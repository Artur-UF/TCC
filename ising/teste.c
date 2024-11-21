#include "lib.h"


int main(){


    int N = 250000;
    int n = 100;
    double *bins = logspace(pow(10, 1), pow(10, N), n);

    printf("lims = %lf %lf\n", 1., 10.);
    printf("log = %lf %lf\n", log10(1), log10(N));

    for(int i = 0; i < n; ++i) printf("%.2lf\n", bins[i]);

    return 0;
}
