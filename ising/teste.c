#include"lib.h"

#define TI 4.16        // Temperatura inicial
#define TF 2.269        // Temperatua final
#define dT -1.0          // Delta T
#define manT 1          // Set Temperature array manually
#define mT {4.16, 3.0, 2.269185}           // Temperature array
#define sizemT 3        // Size of Temerature array if setted manually

int main(){

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
        T = calloc(nT, sizeof(float));
        for(int i = 0; i < nT; i++) T[i] = Taux[i];
        printf("oi, %lf\n", T[0]);
    }

    printf("%lf\n", T[1]);

    return 0;
}

