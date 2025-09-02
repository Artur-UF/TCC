/*
Esse código performa uma simulação do Modelo de Potts-2D de acordo com os parâmetros definidos

As medidas que podem ser feitas nessa versão são:
- Densidade de Energia
- Magnetização
- Correlação Temporal
- Correlação Espacial
- Identificação de clusters
- Geometric domain-size heterogeneity

gcc ising2D.c lib.c -O3 -lm -g -Wall

ELE NÃO CRIA A FOLDER, ELE SÓ RECEBE O NOME DELA E BOTA OS ARQUIVOS LÁ

*/
#include "lib.h"


//----------------INITIAL CONDITIONS---------------------------
#define FOLDER "imgs" // Define o nome da pasta na qual serão guardados os arquivos de saída 
#define SEED 0          // Define a Seed: se 0 pega do relogio do sistema
#define L 500           // Aresta da Rede
#define STEPS 1      // Número de MCS no equilíbrio
#define RND 1           // 0: inicialização da rede toda com spin 1 || 1: inicialização aleatória da rede
#define TI 3.0        // Temperatura inicial
#define TF 1.0        // Temperatua final
#define dT -0.02          // Delta T
#define TRANS 5000      // Número de MCS para jogar fora (transiente)
#define manT 0          // Set Temperature array manually
#define mT {2.3}           // Temperature array
#define sizemT 1        // Size of Temerature array if setted manually
//----------------MEASUREMENTS---------------------------------
#define dM 1          // Passos entre medidas
#define IMG 0           // Para gravar snapshots
#define CI 0            // Para gravar a condição inicial
#define CR 0            // Gravar a Correlação espacial
#define HK 2            // Identificar clusters: 0 não mede, 1 grava só Hg, 2 grava sistema e Hg, > 2 só aplpica HK
#define SNAP 1          // Takes a snapshot of the moment
#define CLS 0           // Saves the size of each cluster
#define A 0             // Measures the average cluster size bigger than 1
#define MES 0           // 0 doesn't mesure Energy and Magnetization and time correlation
#define N1 0            // Counts the number of isolated spins
#define DIST 0          // Generates a distribution of cluster sizes with logarithmic binning
#define HULLH 1         // Measures the heterogeneity of hull sizes

int main(int argc, char *argv[]){
    // Changing stack size for recursive function
    const rlim_t kStackSize = 50L * 1024L * 1024L;   // min stack size = 16 Mb
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
        sprintf(command, "find %s/ -name *%d.dat", FOLDER, seed);
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
    char arkinfo[50], shared[70], saida1[150], saida2[150], saida3[150], saida4[150], saida5[150], saida6[150], saida7[150], saida8[150], saida9[150], saida10[150], saida11[150];
    sprintf(shared, "L_%d_TI_%.2lf_TF_%.2lf_dT_%.2lf_STEPS_%d_RND_%d_TRANS_%d", L, TI, TF, dT, STEPS, RND, TRANS);

    sprintf(arkinfo,         "%s/info.txt", FOLDER);
    sprintf(saida1, "%s/medidas_%s_%d.dat", FOLDER, shared, seed);
    sprintf(saida2,      "%s/im_%s_%d.dat", FOLDER, shared, seed);
    sprintf(saida3,      "%s/ci_%s_%d.dat", FOLDER, shared, seed);
    sprintf(saida4,      "%s/CR_%s_%d.dat", FOLDER, shared, seed);
    sprintf(saida5,      "%s/HK_%s_%d.dat", FOLDER, shared, seed);
    sprintf(saida6,     "%s/CLS_%s_%d.dat", FOLDER, shared, seed);
    sprintf(saida7,    "%s/snap_%s_%d.dat", FOLDER, shared, seed);
    sprintf(saida8,      "%s/n1_%s_%d.dat", FOLDER, shared, seed);
    sprintf(saida9,       "%s/A_%s_%d.dat", FOLDER, shared, seed);
    sprintf(saida10,   "%s/DIST_%s_%d.dat", FOLDER, shared, seed);
    sprintf(saida11,  "%s/HULLH_%s_%d.dat", FOLDER, shared, seed);

    FILE *medidas, *img, *ci, *cr, *hk, *cls, *snap, *n1, *meanA, *fdistri, *hullH;

    if(MES)                medidas = fopen(saida1, "w");
    if(IMG)                img = fopen(saida2, "w");
    if(CI)                 ci = fopen(saida3, "w");
    if(CR > 0)             cr = fopen(saida4, "a");
    if(HK == 1 || HK == 2) hk = fopen(saida5, "w");
    if(CLS && HK > 0)      cls = fopen(saida6, "w");
    if(SNAP)               snap = fopen(saida7, "w");
    if(N1)                 n1 = fopen(saida8, "w");
    if(A)                  meanA = fopen(saida9, "w");
    if(DIST)               fdistri = fopen(saida10, "w");
    if(HULLH)              hullH = fopen(saida11, "w");

    FILE *info = fopen(arkinfo, "a");

    srand(seed);
    //__________________________________SIMULAÇÃO______________________________________________________________

    int pI, i, j, s, t, N = L*L, J = 1, ncr = 0; 
    double beta, E, m0 = 0, mt = 0;
    int stepcr = (CR <= 0) ? STEPS : STEPS/CR;      //Espaçamento entre medidas de C(r) 

    // Definição de temperatura(s)
    int nT;
    double *T = arange(TI, TF+dT, dT);
    double Taux[] = mT;
    if(manT == 0){
        nT = ceil((TF-TI)/dT);
    }
    if(manT == 1){
        free(T);
        nT = sizemT;
        T = calloc(nT, sizeof(double));
        for(int i = 0; i < nT; i++) T[i] = Taux[i];
    }

    // Criando matriz e vetores necessários
    int **viz = vizinhos(L);
    int *sis = (int*)calloc(N, sizeof(int));
    int *s0 = (int*)calloc(N, sizeof(int));
    double *crr = (double*)calloc(L/2, sizeof(double));
    double *expBeta = (double*)calloc(3, sizeof(double));
    int *hksis = (int*)calloc(N, sizeof(int));              // Saves the labelled system
    int *hksize = (int*)malloc(N*sizeof(int));              // Saves the cluster size of each label
    int *hg = (int*)calloc(N, sizeof(int));                 // Aux to the function that calculates H
    double *distri = (double *)calloc(N, sizeof(double));   // Saves the distribution of cluster sizes
    int *nonperc = (int *)malloc(N*sizeof(int));            // stores the label of clusters not touching the lattice walls
    int *hullsize = (int *)calloc(N, sizeof(int));           // stores the distribution of hull sizes

    if(MES == 0) free(s0);
    if(CR == 0) free(crr);

    // Aplicando a Condição inicial
    if(RND) for(i = 0; i < N; ++i){
        pI = (int)uniform(0., 3.);
        switch(pI){
            case 0:
                sis[i] = pI;
            break;
            case 1:
                sis[i] = pI;
            break;
            case 2:
                sis[i] = pI;
            break;
        }
    }
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
            for(j = 0; j < N; ++j) metropolis(sis, viz, &E, expBeta, J, j);
            // se quiser gravar o transiente vc faria aqui
        }
        // Fim do loop transiente

        // Definindo s(t=0) e m(t=0)
        if(s == TRANS && MES > 0){
            for(i = 0; i < N; ++i) s0[i] = sis[i];
            m0 = magnetizacao(sis, N);
        }
        if(MES > 0) fprintf(medidas, "# %.4lf\n", T[temp]);

        if(DIST) fprintf(fdistri, "# %.4lf\n", T[temp]);
 
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
            if(MES > 0 && s%dM == 0){
                mt = magnetizacao(sis, N);
                fprintf(medidas, "%lf %lf %lf\n", E/N, mt, corrtemp(s0, sis, m0, mt, N));
                if((CR > 0) && (ncr < CR) && (s%stepcr == 0)){
                    corresp(crr, sis, viz, N, L, mt);
                    for(int l  = 0; l < L/2; ++l) fprintf(cr, "%d\t%lf\n", l+1, crr[l]);
                    fprintf(cr, "-1\t-1\n");
                    memset(crr, 0, (L/2)*sizeof(double));
                    ncr++;
                }
            }
            // Geometric measurements
            if(s%dM == 0){
                if(HK > 0){
                    // Saves a snapshot of the system 
                    if(SNAP){
                        for(int i = 0; i < N; ++i) fprintf(snap, "%d\n", sis[i]);
                        fprintf(snap, "0\n");
                    }
                    hoshenkopelman(sis, viz, hksis, hksize, N);
                    // Saves the Hg and the system with labeled clusters
                    if(HK == 1 || HK == 2)fprintf(hk, "# %d %.4lf\n", Hg(hksize, hg, N), T[temp]);
                    if(HK == 2) for(int i = 0; i < N; ++i) fprintf(hk, "%d\n", hksis[i]);
                    // Measures the mean size of clusters bigger than 1
                    if(A) fprintf(meanA, "%lf %lf\n", T[temp], meansize(hksize, N));
                    if(HULLH){
                        find_non_percolating_clusters(nonperc, hksis, hksize, viz, L);
                        for(int i = 0; i < N; ++i) if(nonperc[i] > 0) hullsize[mc_winding(i, hksis, viz, nonperc[i])]++;
                        fprintf(hullH, "%lf %d\n", T[temp], hull_H(hullsize, N));
                        memset(hullsize, 0, N*sizeof(int));
                    }
                }
                // Saves the size of each cluster
                if(CLS){
                    hoshenkopelman(sis, viz, hksis, hksize, N);
                    fprintf(cls, "# %d %.4lf\n", Hg(hksize, hg, N), T[temp]);
                    for(int i = 0; i < N; ++i) if(hksize[i] > 0) fprintf(cls, "%d %d\n", i, hksize[i]);
                }
                if(N1) fprintf(n1, "%lf %lf\n", T[temp], lonelyspins(sis, viz, N)/N);
                if(DIST) for(int i = 0; i < N; i++) if(hksize[i] > 0) distri[hksize[i]] += 1.;
            }
        }
        if(DIST){
            for(int i = 0; i < N; ++i){
                if(distri[i] > 0.){
                    fprintf(fdistri, "%d %lf\n", i, distri[i]/((double) STEPS/dM));
                    distri[i] = 0.;
                }
            }
        }
    }
    clock_t toc = clock();
    double time = (double)(toc-tic)/CLOCKS_PER_SEC;

    //_________________________________FIM DA SIMULAÇÃO_____________________________________________

    fprintf(info, "-*-*-*-*-*-*-| NEW RUN |-*-*-*-*-*-*-*-*-*\n");
    fprintf(info,    "SEED %d\n", seed);
    fprintf(info,       "L %d\n", L);
    fprintf(info,   "STEPS %d\n", STEPS);
    fprintf(info,     "RND %d\n", RND);
    fprintf(info,     "TI %lf\n", TI);
    fprintf(info,     "TF %lf\n", TF);
    fprintf(info,     "dT %lf\n", dT);
    fprintf(info,   "TRANS %d\n", TRANS);
    fprintf(info,      "dM %d\n", dM);
    fprintf(info,    "manT %d\n", manT);
    fprintf(info,  "sizemT %d\n\n", sizemT);
    fprintf(info, "Execution time: %.3lf s | %.3lf min | %.3lf h\n", time, time/60., time/3600.);

    free(viz);
    free(sis);
    free(expBeta);
    free(hksis);
    free(hksize);
    free(hg);
    free(distri);
    free(nonperc);
    free(hullsize);
    if(MES != 0) free(s0);
    if(CR != 0) free(crr);

    if(MES)                fclose(medidas);
    if(IMG)                fclose(img);
    if(CI)                 fclose(ci);
    if(CR > 0)             fclose(cr);
    if(HK == 1 || HK == 2) fclose(hk);
    if(CLS && HK > 0)      fclose(cls);
    if(SNAP)               fclose(snap);
    if(N1)                 fclose(n1);
    if(A)                  fclose(meanA);
    if(DIST)               fclose(fdistri);
    if(HULLH)              fclose(hullH);
    fclose(info);

    return 0;
}

