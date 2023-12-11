/*

Esse código performa uma simulação do Modelo de Ising-2D de acordo com os parâmetros definidos

As medidas que podem ser feitas nessa versão são:
- Densidade de Energia
- Magnetização
- Correlação Temporal
- Correlação Espacial
- Identificação de clusters
- Geometric domain-size heterogeneity

gcc ising2D.c lib.c -O3 -lm

ELE NÃO CRIA A PASTA, ELE SÓ RECEBE O NOME DELA E BOTA OS ARQUIVOS LÁ

1702084705 - SEGFAULT em T = 2.0
1702064765 - SEGFAULT em T = 1.0
1702069689 - SEGFAULT em T = 1.0
1702079013 - SEGFAULT em T = 1.5
1702100969 - SEGFAUÇT em T = 2.0
1702103491 - SEGFAULT em T = 1.5
1702107985 - SEGFAULT em T = 2.0

*/
#include "lib.h"

#define PASTA "samples_L_640" // Define o nome da pasta na qual serão guardados os arquivos de saída 
#define SEED 1702107985          // Define a Seed: se 0 pega do relogio do sistema
#define L 640           // Aresta da Rede
#define STEPS 1000      // Número de MCS no equilíbrio
#define RND 1           // 0: inicialização da rede toda com spin 1 || 1: inicialização aleatória da rede
#define IMG 0           // Para gravar snapshots
#define CI 0            // Para gravar a condição inicial
#define TI 1.        // Temperatura inicial
#define TF 10.        // Temperatua final
#define dT 0.5          // Delta T
#define TRANS 5000      // Número de MCS para jogar fora (transiente)
#define CR 0            // Gravar a Correlação espacial
#define HK 2            // Identificar clusters: 0 não mede, 1 mede tudo, 2 mede só o Hg
#define SNAP 0          // Takes a snapshot of the moment
#define CLS 0           // Saves the size of each cluster
#define MES 0

int main(int argc, char *argv[]){
    int seed;
    if(SEED == 0){
        seed = time(NULL);
        if(seed%2 == 0) seed++;
    }
    else seed = SEED; 

    // Opennig output files
    int ok = 0;
    char arkinfo[50], shared[70], saida1[150], saida2[150], saida3[150], saida4[150], saida5[150], saida6[150], saida7[150];
    sprintf(shared, "L_%d_TI_%.2lf_TF_%.2lf_dT_%.2lf_STEPS_%d_RND_%d_TRANS_%d", L, TI, TF, dT, STEPS, RND, TRANS);

    FILE *medidas;
    do{
        sprintf(saida1, "%s/medidas_%s_%d.dat", PASTA, shared, seed);
        medidas = fopen(saida1, "r");
        if(medidas != NULL){
            seed += 2;
            fclose(medidas);
        }
        else ok = 1;
    }while(ok == 0);

    // Fazer o arquivo de infos que recebe append

    sprintf(arkinfo, "%s/info.txt", PASTA);
    sprintf(saida2,      "%s/im_%s_%d.dat", PASTA, shared, seed);
    sprintf(saida3,      "%s/ci_%s_%d.dat", PASTA, shared, seed);
    sprintf(saida4,      "%s/CR_%s_%d.dat", PASTA, shared, seed);
    sprintf(saida5,      "%s/HK_%s_%d.dat", PASTA, shared, seed);
    sprintf(saida6,     "%s/CLS_%s_%d.dat", PASTA, shared, seed);
    sprintf(saida7,    "%s/snap_%s_%d.dat", PASTA, shared, seed);

    medidas = fopen(saida1, "a");
    FILE *img = fopen(saida2, "w");
    FILE *ci = fopen(saida3, "w");
    FILE *cr = fopen(saida4, "a");
    FILE *hk = fopen(saida5, "w");
    FILE *cls = fopen(saida6, "w");
    FILE *snap = fopen(saida7, "w");

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
    double *expBeta = (double*)calloc(3, sizeof(int));
    int *hksis = (int*)calloc(N, sizeof(int));
    int *hksize = (int*)malloc(N*sizeof(int));
    int *hg = (int*)calloc(N, sizeof(int));

    // Aplicando a Condição inicial
    if(RND) for(i = 0; i < N; ++i) sis[i] = (uniform(0., 1.) < .5) ? -1 : 1;
    else for(i = 0; i < N; ++i) sis[i] = 1;
    
    if(CI) for(i = 0; i < N; ++i) fprintf(ci, "%d\n", sis[i]);  

    // Simulação
    clock_t tic = clock();

    t = 0;
    for(int temp = 0; temp <= nT; ++temp){      // Loop de temperaturas
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
            printf("T = %.2lf\n", T[temp]);
            hoshenkopelman(sis, viz, hksis, hksize, N);
            printf("Feito\n");
            // Saves the Hg and the system with labeled clusters
            fprintf(hk, "# %d\n", Hg(hksize, hg, N));
            if(HK == 1) for(int i = 0; i < N; ++i) fprintf(hk, "%d\n", hksis[i]);
            // Saves the size of each cluster
            if(CLS) for(int i = 0; i < N; ++i) if(hksize[i] > 0) fprintf(cls, "%d %d\n", i, hksize[i]);
        }
    }
    clock_t toc = clock();
    double time = (double)(toc-tic)/CLOCKS_PER_SEC;

    //_________________________________FIM DA SIMULAÇÃO_____________________________________________ 
    fprintf(medidas, "-1\t-1\t-1\t-1\n"); 

    fprintf(info, "-*-*-*-*-*-*-| NEW RUN |-*-*-*-*-*-*-*-*-*\n");
    fprintf(info,    "SEED %d\n", seed);
    fprintf(info,       "L %d\n", L);
    fprintf(info,   "STEPS %d\n", STEPS);
    fprintf(info,     "RND %d\n", RND);
    fprintf(info,     "TI %lf\n", TI);
    fprintf(info,     "TF %lf\n", TF);
    fprintf(info,     "dT %lf\n", dT);
    fprintf(info, "TRANS %d\n\n", TRANS);
    fprintf(info, "Execution time: %lf s | %lf min\n", time, time/60.);
 
    fclose(info); 
    fclose(medidas);
    fclose(img);
    fclose(ci);
    fclose(cr);
    fclose(hk);
    if(MES == 0) remove(saida1);
    if(!IMG) remove(saida2);
    if(!CI) remove(saida3);
    if(CR == 0) remove(saida4);
    if(HK == 0) remove(saida5);
    if(CLS == 0) remove(saida6);
    if(SNAP == 0) remove(saida7);

    return 0;
}

