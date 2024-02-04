#!/usr/bin/python3
import os
import sys
import numpy as np

def definer(ark, *args):
    '''
    Recebe um arquvio .c e edita os #defines com os argumetos dados nessa ordem:
    PASTA, SEED, L, STEPS, RND, IMG, CI, TI, TF, dT, TRANS, CR, HK, SNAP, CLS, MES, N1
    '''
    with open(ark, 'r') as f:
        linhas = f.readlines()
    
    params = {'PASTA':args[0],
            'SEED':f'{args[1]}',
            'L':f'{args[2]}',
            'STEPS':f'{args[3]}',
            'RND':f'{args[4]}',
            'IMG':f'{args[5]}',
            'CI':f'{args[6]}',
            'TI':f'{args[7]:.3f}',
            'TF':f'{args[8]:.3f}',
            'dT':f'{args[9]:.3f}',
            'TRANS':f'{args[10]}',
            'CR':f'{args[11]}', 
            'HK':f'{args[12]}', 
            'SNAP':f'{args[13]}', 
            'CLS':f'{args[14]}', 
            'MES':f'{args[15]}', 
            'N1':f'{args[16]}'}

    with open(ark, 'w') as f:
        for l in range(len(linhas)):
            var = linhas[l].split(' ')
            if var[0] == '#define':
                var[2] = params[var[1]]
            f.write(' '.join(var))


PASTA = r'"hk_640_0"'
SEED = 0
L = 640
STEPS = 1000
RND = 1     
IMG = 0     
CI = 0
TRANS = 5000
CR = 0      
HK = 2  
SNAP = 0
CLS = 0 
MES = 0 
N1 = 0  

#------------Definindo temperaturas-----------
ti = 4
tf = 5
ts, step = np.linspace(ti, tf, 4, retstep=True)
TS, dT = np.linspace(ti+step/2, tf-step/2, 3, retstep=True)
      
TI = TS[0]
TF = TS[-1]

definer('ising2D.c', PASTA, SEED, L, STEPS, RND, IMG, CI, TI, TF, dT, TRANS, CR, HK, SNAP, CLS, MES, N1)

for i in range(4):
    os.mkdir(f'hk_{L}_{i}')

    os.system('make out')
    
    for i in range(25):
        os.system('./out_find &')
        os.system('./out_find &')
        os.system('./out_find &')
        os.system('./out_find')
    
    samples = fnmatch.filter(list(i.name for i in os.scandir(path)), 'HK*')
    
    if len(samples) < 100:
        resto = 100 - len(samples)
        for i in range(resto):
            os.system('./out_find')
    
    os.system('make clean')
    
    os.system(f'python3 filter_hg.py {L} {TI:.4f} {TF:.4f} {dT} {i}')
    break    
    t = np.loadtxt(f'hk_{L}_{i}.dat')

    #--------------------Novas temperaturas--------------------
    ti = ts[np.where(t == max(t))[0]]
    tf = ts[np.where(t == max(t))[0]+1]
    ts, step = np.linspace(ti, tf, 4, retstep=True)
    TS, dT = np.linspace(ti+step/2, tf-step/2, 3, retstep=True)
    
    TI = TS[0]
    TF = TS[-1]
    
    PASTA = f'\"hk_{L}_{i+1}\"'
    
    definer('ising2D.c', PASTA, SEED, L, STEPS, RND, IMG, CI, TI, TF, dT, TRANS, CR, HK, SNAP, CLS, MES, N1)

