/*
Library with usefull functions for Monte Carlo and Ising-2D
*/
#include"lib.h"


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

double uniform(double min, double max) {
    /*
    Function that generates a random number with a uniform distribution
    For int: [min, max)
    */
    double random  = ((double) rand()) / RAND_MAX;
    double range = (max - min) * random;
    double n = range + min;

    return n;
}

int **vizinhos(int L){
    int N = L*L;
    int **mtzviz = (int **)malloc(N*sizeof(int*));
    for(int n = 0; n < N; ++n){
        mtzviz[n] = (int *)malloc(4*sizeof(int));
    }
    /*
    mtzviz[i][0] - right
    mtzviz[i][1] - up
    mtzviz[i][2] - left
    mtzviz[i][3] - down
    */

    for(int i = 0; i < N; ++i){  
        // ultima coluna, deslocamos  L-1
        if(i%L == L-1) mtzviz[i][0] = i + 1 - L;
        else mtzviz[i][0] = i + 1;
        // primeira coluna, somamos L-1
        if(i%L == 0) mtzviz[i][2] = i - 1 + L;
        else mtzviz[i][2] = i - 1;
        // primeira linha, somamos N-L
        if(i<L) mtzviz[i][1] = i - L + N;
        else mtzviz[i][1] = i - L;
        // ultima linha, modulo L
        if(i>=N-L) mtzviz[i][3] = (i % L);
        else mtzviz[i][3] = i + L;
    }
    return mtzviz;
}

void defexp(double *expBeta, double beta){
   expBeta[0] = exp(-beta*0);
   expBeta[1] = exp(-beta*4);
   expBeta[2] = exp(-beta*8);
}

void metropolis(int *sis, int **viz, double *E, double *expBeta, int J, int j){
    /*
    Apply the Metropolis algorithm
    */
    int dE = 2*J*sis[j]*(sis[viz[j][0]] + sis[viz[j][1]] + sis[viz[j][2]] + sis[viz[j][3]]);
    if((dE < 0) || (uniform(0., 1.) < expBeta[dE/4])){
        sis[j] *= -1;
        *E += dE;
    }
}

int energia(int *sis, int **viz, int N, int j){
    /*
    Mesures the energy of the system
    */
    int en = 0;
    for(int i = 0; i < N; ++i) en += sis[i]*(sis[viz[i][0]] + sis[viz[i][3]]);
    return -j*en;
}

double magnetizacao(int *sis, int N){
    /*
    Mesures the magnetization of the system
    */
    double m = 0;
    for(int i = 0; i < N; ++i) m += sis[i];
    return m/N;
}

double corrtemp(int *s0, int *st, double m0, double mt, int N){
    /*
    Mesures the time correlation of the system
    */
    double C = 0;
    for(int i = 0; i < N; ++i){
        C += s0[i]*st[i];
    }
    C /= N;
    C -= m0*mt;
    return C;
}

void corresp(double *crr, int *s, int **viz, int N, int L, double m){
    /*
    Mesures the espacial correlation of the  system
    */
    double c = 0;
    int vv, vh;
    for(int i = 0; i < N; ++i){
        vv = viz[i][3];
        vh = viz[i][0];
        for(int l = 0; l < L/2; ++l){
            c = s[i]*(s[vh] + s[vv]);
            vv = viz[vv][3];
            vh = viz[vh][0];
            crr[l] += c; 
        }
    }
    for(int l = 0; l < L/2; ++l){
        crr[l] /= 2*N;
        //crr[l] -= m*m;
    }
}

void hoshenkopelman(int *sis, int **viz, int *hk, int *hksize, int N){
    // First assignment of values
    for(int i = 0; i < N; ++i) hk[i] = i;

    // Union of clusters
    for(int i = 0; i < N; ++i){
        if(sis[i] == sis[viz[i][1]]){
            unionfind(i, viz[i][1], hk, viz);
        }
        if(sis[i] == sis[viz[i][2]]){
            unionfind(i, viz[i][2], hk, viz);
        }
    }

    // Mesure size of clusters
    memset(hksize, 0, N*sizeof(*hksize));
    for(int i = 0; i < N; ++i) hksize[hk[i]] += 1;
}

void unionfind(int i, int j, int *hk, int **viz){
/*
Decides wich label to use and then calls a recursive function
to change the label
*/

    if(hk[i] > hk[j]) recurlabel(hk, viz, i, hk[i], hk[j]);
    if(hk[i] < hk[j]) recurlabel(hk, viz, j, hk[j], hk[i]);
}

void recurlabel(int *hk, int **viz, int i, int labeli, int labelf){
/*
Searches recursively for more labels of the same value and then finally
changes all of them
*/
    if(-hk[viz[i][0]] == -labeli){
        hk[i] *= -1; 
        recurlabel(hk, viz, viz[i][0], labeli, labelf);
    }
    if(-hk[viz[i][1]] == -labeli){
        hk[i] *= -1;
        recurlabel(hk, viz, viz[i][1], labeli, labelf);
    }
    if(-hk[viz[i][2]] == -labeli){
        hk[i] *= -1;
        recurlabel(hk, viz, viz[i][2], labeli, labelf);
    }
    if(-hk[viz[i][3]] == -labeli){
        hk[i] *= -1;
        recurlabel(hk, viz, viz[i][3], labeli, labelf);
    }
    hk[i] = labelf;
}

int Hg(int *hksize, int *hg, int N){
/*
Counts the number of different domain-sizes of clusters
*/
    int Hg = 0;
    for(int i = 0; i < N; ++i){
        if(hksize[i] > 0 && hg[hksize[i]] == 0){ 
            hg[hksize[i]] = 1;
            Hg++;
        }
    }
    memset(hg, 0, N*sizeof(*hg));
    return Hg;
}


double lonelyspins(int *sys, int **fn, int N){
/*
Counts the number of isolated spins of a system
*/
    int n1 = 0;
    for(int i = 0; i < N; ++i) if((sys[fn[i][0]] + sys[fn[i][1]] + sys[fn[i][2]] + sys[fn[i][3]])*sys[i] == -4) ++n1;
    return n1;
}


double meansize(int *hksize, int N){
/*
 Averages the sizes of clusters bigger than 1
 */
    double A = 0., countclusters = 0.;

    for(int i = 0; i < N; ++i){
        if(hksize[i] > 1){
            A += (double) hksize[i];
            countclusters++;
        }
    }
    return A/countclusters;
}


double *logspace(double a, double b, int n){
/*
 Creates an even-spaced array in log10 scale within the interval [a, b]
*/
    double *array = (double *)calloc(n, sizeof(double));
    double a0 = log10(a), b0 = log10(b);
    double ds = (b0-a0)/(n-1);
    for(int i = 0; i < n; ++i) array[i] = pow(10, a0+(i*ds));
    return array;
}

int mc_winding(int qual, int *hk, int **nmtx, int size){
    if(size == 1) return 4;
    int i=0,dir,ok,sitesonhull=0,endofwalk,firststep;

    // Direction (dir): 0 (up), 1 (left), 2 (down), 3 (right)
    endofwalk = 0;
    dir = 3;
    i = qual;
    firststep = 1;
    while (!endofwalk){
        ok = 0;
        dir = (dir+1)%4;  // from the incoming direction, try left first
        while (!ok){ // from the incoming direction: try right, in front, left and backwards
            switch (dir){
		case 0:
                    if(hk[nmtx[i][1]] == hk[i]){
		        ok = 1;
            	        i = nmtx[i][1];
            	    }
                    else{
                        if((i==qual) && (!firststep)){
                            endofwalk = 1;
                            break;
			}
            	        ++sitesonhull;
                        firststep = 0;
            	    }
            	    break;
            	case 1:
		    if(hk[nmtx[i][2]] == hk[i]) {
			ok = 1;
 	        	i = nmtx[i][2];
            	    }
            	    else{
            	    	++sitesonhull;
            	    }
            	    break;
            	case 2:
		    if(hk[nmtx[i][3]] == hk[i]) {
			ok = 1;
            	    	i = nmtx[i][3];
            	    }
            	    else{
            	     	++sitesonhull;
            	    }
            	    break;
            	case 3:
		    if(hk[nmtx[i][0]] == hk[i]) {
			ok = 1;
            	    	i = nmtx[i][0];
            	    }
          	    else{
            	    	++sitesonhull;
            	    }
            	    break;
	    }
	    if(ok==0) dir = (dir + 3)%4;
	}
    }
    return sitesonhull;
}


int find_biggest_cluster(int *hksize, int N){
    int label = 0, size = 0;
    for(int i = 0;i < N; ++i){
        if(hksize[i] > size){
            label = i;
            size = hksize[i];
        }
    }
    return label;
}

void find_non_percolating_clusters(int *nonperc, int *hk, int *hksize, int **nmtx, int L){
    for(int i = 0; i < L*L; i++) nonperc[i] = hksize[i];

    int i = 0, dir = 1;

    for(int j = 0; j < 4*(L-1); ++j){
        nonperc[hk[i]] = 0;
        if(i%(L-1) == 0){
            dir = (dir+3)%4;
        }
        i = nmtx[i][dir];
    }
    return;
}

int hull_H(int *hullsize, int N){
    int hullH = 0;
    for(int i = 0; i < N; i++) if(hullsize[i] > 0) hullH++;
    return hullH;
}



