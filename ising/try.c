#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(){
    double *arange(double i, double f, double s);

    double i = 1., f = 1., s = 0.5;
    int n = ceil((f-i)/s);

    double *array = arange(i, f+s, s);

    for(int i = 0; i <= n; ++i) printf("%lf\n", array[i]);
    return 0;
}



double *arange(double i, double f, double s){
/*
Creates an array of size: ceil((f-i)/s) with 's' as step size
*/
    int n = ceil((f-i)/s);
    double *array = (double*)malloc(n*sizeof(double));
    for(int ni = 0; ni < n; ni++){
        array[ni] = i;
        i += s;
    }
    return array;
}
