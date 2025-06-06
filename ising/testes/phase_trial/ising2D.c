/*
Esse código performa uma simulação do Modelo de Ising-2D de acordo com os parâmetros definidos

As medidas que podem ser feitas nessa versão são:
- Densidade de Energia
- Magnetização
- Correlação Temporal
- Correlação Espacial
- Identificação de clusters
- Geometric domain-size heterogeneity

gcc ising2D.c lib.c -O3 -lm -g -Wall

ELE NÃO CRIA A PASTA, ELE SÓ RECEBE O NOME DELA E BOTA OS ARQUIVOS LÁ

*/
#include "lib.h"

#define PASTA "hk_640_1" // Define o nome da pasta na qual serão guardados os arquivos de saída 
#define SEED 0          // Define a Seed: se 0 pega do relogio do sistema
#define L 640           // Aresta da Rede
#define STEPS 1000      // Número de MCS no equilíbrio
#define RND 1           // 0: inicialização da rede toda com spin 1 || 1: inicialização aleatória da rede
#define IMG 0           // Para gravar snapshots
#define CI 0            // Para gravar a condição inicial
#define TI 4.556        // Temperatura inicial
#define TF 4.778        // Temperatua final
#define dT 0.111          // Delta T
#define TRANS 5000      // Número de MCS para jogar fora (transiente)
#define CR 0            // Gravar a Correlação espacial
#define HK 2            // Identificar clusters: 0 não mede, 1 mede tudo, 2 mede só o Hg
#define SNAP 0          // Takes a snapshot of the moment
#define CLS 0           // Saves the size of each cluster
#define MES 0           // 0 doesn't mesure Energy and Magnetization and time correlation
#define N1 0            // Counts the number of isolated spins


int main(int argc, char *argv[]){
    // Changing stack size for recursive function
    const rlim_t kStackSize = 32L * 1024L * 1024L;   // min stack size = 16 Mb
    struct rlimit rl;
    int result;
    result = getrlimit(RLIMIT_STACK, &rl);
    if (result == 0)
    {
        if (rl.rlim_cur < kStackSize)
        {
            rl.rlim_cur = kStackSize;
            result = setrlimit(RLIMIT_STACK, &rl);
            if (result != 0)
            {
                fprintf(stderr, "setrlimit returned result = %d\n", result);
            }
        }
    }

    int seed;
    if(SEED == 0){
        seed = time(NULL);
        if(seed%2 == 0) seed++;
    }
    else seed = SEED; 

    // Testing seed existence
    FILE *readfile;
    char command[50], buffer[BUFSIZ + 1] = {0};
    int chars_read;
    int ok = 0;
    do{ 
        sprintf(command, "find %s/ -name *%d.dat", PASTA, seed);
        readfile = popen(command, "r");
        chars_read = fread(buffer, sizeof(char), BUFSIZ+1, readfile);
        if(chars_read > 0){
            seed += 2;
        }else{
            ok = 1;
        }
        memset(buffer, 0, (BUFSIZ +1)*sizeof(char));
        memset(command, 0, 50*sizeof(char));
        pclose(readfile);
    }while(ok == 0);

    // Openning output files
    char arkinfo[50], shared[70], saida1[150], saida2[150], saida3[150], saida4[150], saida5[150], saida6[150], saida7[150], saida8[150];
    sprintf(shared, "L_%d_TI_%.2lf_TF_%.2lf_dT_%.2lf_STEPS_%d_RND_%d_TRANS_%d", L, TI, TF, dT, STEPS, RND, TRANS);

    sprintf(arkinfo,         "%s/info.txt", PASTA);
    sprintf(saida1, "%s/medidas_%s_%d.dat", PASTA, shared, seed);
    sprintf(saida2,      "%s/im_%s_%d.dat", PASTA, shared, seed);
    sprintf(saida3,      "%s/ci_%s_%d.dat", PASTA, shared, seed);
    sprintf(saida4,      "%s/CR_%s_%d.dat", PASTA, shared, seed);
    sprintf(saida5,      "%s/HK_%s_%d.dat", PASTA, shared, seed);
    sprintf(saida6,     "%s/CLS_%s_%d.dat", PASTA, shared, seed);
    sprintf(saida7,    "%s/snap_%s_%d.dat", PASTA, shared, seed);
    sprintf(saida8,      "%s/n1_%s_%d.dat", PASTA, shared, seed);


    FILE *medidas, *img, *ci, *cr, *hk, *cls, *snap, *n1;

    if(MES)           medidas = fopen(saida1, "a");
    if(IMG)           img = fopen(saida2, "w");
    if(CI)            ci = fopen(saida3, "w");
    if(CR > 0)        cr = fopen(saida4, "a");
    if(HK > 0)        hk = fopen(saida5, "w");
    if(CLS && HK > 0) cls = fopen(saida6, "w");
    if(SNAP)          snap = fopen(saida7, "w");
    if(N1)            n1 = fopen(saida8, "w");

    FILE *info = fopen(arkinfo, "a");

    srand(seed);
    //__________________________________SIMULAÇÃO______________________________________________________________

    int i, j, s, t, N = L*L, J = 1, ncr = 0; 
    double beta, E, m0 = 0, mt = 0;
    int stepcr = (CR <= 0) ? STEPS : STEPS/CR;      //Espaçamento entre medidas de C(r) 

    // Definição de temperatura(s)
    int nT = ceil((TF-TI)/dT);
    double *T = arange(TI, TF+dT, dT);

    // Criando matriz e vetores necessários
    int **viz = vizinhos(L);
    int *sis = (int*)calloc(N, sizeof(int));
    int *s0 = (int*)calloc(N, sizeof(int));
    double *crr = (double*)calloc(L/2, sizeof(double));
    double *expBeta = (double*)calloc(3, sizeof(double));
    int *hksis = (int*)calloc(N, sizeof(int));
    int *hksize = (int*)malloc(N*sizeof(int));
    int *hg = (int*)calloc(N, sizeof(int));

    if(MES == 0) free(s0);
    if(CR == 0) free(crr); 

    // Aplicando a Condição inicial
    if(RND) for(i = 0; i < N; ++i) sis[i] = (uniform(0., 1.) < .5) ? -1 : 1;
    else for(i = 0; i < N; ++i) sis[i] = 1;
    
    if(CI) for(i = 0; i < N; ++i) fprintf(ci, "%d\n", sis[i]);  

    // Simulação
    clock_t tic = clock();

    t = 0;
    for(int temp = 0; temp < nT; ++temp){      // Loop de temperaturas
        beta = 1./T[temp];
        defexp(expBeta, beta);
        // Loop para passar pelo transiente
        E = (double) energia(sis, viz, N, 1);
        for(s = 0; s < TRANS; ++s){ //Loop sobre passos de Monte Carlo
            //MCS
            for(j = 0; j < N; ++j){
                metropolis(sis, viz, &E, expBeta, J, j);
            }
            // se quiser gravar o transiente vc faria aqui
        }
        // Fim do loop transiente

        // Definindo s(t=0) e m(t=0)
        if(s == TRANS && MES > 0){
            for(i = 0; i < N; ++i) s0[i] = sis[i];
            m0 = magnetizacao(sis, N);
        }

        // Roda STEPS de MCS no equilíbrio
        for(s = 0; s < STEPS; ++s){
            //MCS
            for(j = 0; j < N; ++j){
                metropolis(sis, viz, &E, expBeta, J, j);
            }
            t++;
            //Fim do MCS
    
            // Imagens para fazer o gif
            if(IMG){
                for(i = 0; i < N; ++i) fprintf(img, "%d\n", sis[i]);
                fprintf(img, "-2\n");
            }

            // Medidas
            if(MES > 0){
                mt = magnetizacao(sis, N);
                fprintf(medidas, "%d\t%lf\t%lf\t%lf\n", t, E/N, mt, corrtemp(s0, sis, m0, mt, N));
                if((CR > 0) && (ncr < CR) && (s%stepcr == 0)){
                    corresp(crr, sis, viz, N, L, mt);
                    for(int l  = 0; l < L/2; ++l) fprintf(cr, "%d\t%lf\n", l+1, crr[l]);
                    fprintf(cr, "-1\t-1\n");
                    memset(crr, 0, (L/2)*sizeof(double));
                    ncr++;
                }
            }
        }
        if(HK > 0){
            // Saves a snapshot of the system 
            if(SNAP){
                for(int i = 0; i < N; ++i) fprintf(snap, "%d\n", sis[i]);
                fprintf(snap, "-2\n");
            }
            hoshenkopelman(sis, viz, hksis, hksize, N);
            // Saves the Hg and the system with labeled clusters
            fprintf(hk, "# %d %.3lf\n", Hg(hksize, hg, N), T[temp]);
            if(HK == 1) for(int i = 0; i < N; ++i) fprintf(hk, "%d\n", hksis[i]);
            // Saves the size of each cluster
            if(CLS){
                for(int i = 0; i < N; ++i) if(hksize[i] > 0) fprintf(cls, "%d %d\n", i, hksize[i]);
                fprintf(cls, "# %.2lf\n", T[temp]);
            }
        }

        if(N1) fprintf(n1, "%lf\n", lonelyspins(sis, viz, N)/N);

    }
    clock_t toc = clock();
    double time = (double)(toc-tic)/CLOCKS_PER_SEC;

    //_________________________________FIM DA SIMULAÇÃO_____________________________________________ 
    if(MES) fprintf(medidas, "-1\t-1\t-1\t-1\n"); 

    fprintf(info, "-*-*-*-*-*-*-| NEW RUN |-*-*-*-*-*-*-*-*-*\n");
    fprintf(info,    "SEED %d\n", seed);
    fprintf(info,       "L %d\n", L);
    fprintf(info,   "STEPS %d\n", STEPS);
    fprintf(info,     "RND %d\n", RND);
    fprintf(info,     "TI %lf\n", TI);
    fprintf(info,     "TF %lf\n", TF);
    fprintf(info,     "dT %lf\n", dT);
    fprintf(info, "TRANS %d\n\n", TRANS);
    fprintf(info, "Execution time: %.3lf s | %.3lf min | %.3lf h\n", time, time/60., time/3600.);

    free(viz);
    free(sis);
    free(s0);
    free(crr);
    free(expBeta);
    free(hksis);
    free(hksize);
    free(hg);

    if(MES)           fclose(medidas);
    if(IMG)           fclose(img);
    if(CI)            fclose(ci);
    if(CR > 0)        fclose(cr);
    if(HK > 0)        fclose(hk);
    if(CLS && HK > 0) fclose(cls);
    if(SNAP)          fclose(snap);
    if(N1)            fclose(n1);
    fclose(info);

    return 0;
}

