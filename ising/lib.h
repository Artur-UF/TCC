#ifndef _LIB_H_
#define _LIB_H_

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <sys/stat.h>
#include <string.h>
#include <stdbool.h>

int **vizinhos(int l);

void defexp(double *expBeta, double beta); 

void metropolis(int *sis, int **viz, double *E, double *beta, int J, int j);

int energia(int *sis, int **viz, int n, int j);

double magnetizacao(int *sis, int n);

double uniform(double min, double max);

double corrtemp(int *s0, int *st, double m0, double mt, int n);

void corresp(double *cr, int *s, int **viz, int n, int l, double m);

void hoshenkopelman(int **viz, int *sis, int *hksis, int l);


#endif
