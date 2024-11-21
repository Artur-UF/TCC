#ifndef _LIB_H_
#define _LIB_H_

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <sys/stat.h>
#include <string.h>
#include <stdbool.h>
#include <sys/resource.h>

int **vizinhos(int L);

double *arange(double i, double f, double s);

void defexp(double *expBeta, double beta); 

void metropolis(int *sis, int **viz, double *E, double *beta, int J, int j);

int energia(int *sis, int **viz, int n, int j);

double magnetizacao(int *sis, int N);

double uniform(double min, double max);

double corrtemp(int *s0, int *st, double m0, double mt, int N);

void corresp(double *cr, int *s, int **viz, int N, int L, double m);

void hoshenkopelman(int *sis, int **viz, int *hk, int *hksize, int N);

void unionfind(int i, int j, int *hk, int **viz);

void recurlabel(int *hk, int **viz, int i, int labeli, int labelf);

int Hg(int *hksize, int *hg, int N);

double lonelyspins(int *sys, int **fn, int N);

double meansize(int *hksize, int N);

double *logspace(double a, double b, int n);

#endif
