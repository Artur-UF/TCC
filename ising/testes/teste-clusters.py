#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import sys
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 12})

def split0(array, flag):
    '''
    Faz a separação de um array numérico de acordo com uma flag numérica
    '''
    arrnd = list()
    a = list()
    for i in range(len(array)):
        if array[i] == flag and type(flag) == int:
            arrnd.append(a)
            a = list()
        else: a.append(array[i])
    arrnd.append(a)
    return arrnd[:-1]

def split(array):
    '''
    Faz a separação de um array numérico de acordo com uma flag numérica
    '''
    arrnd = list()
    a = list()
    for i in range(len(array)):
        if array[i] < 0:
            if len(a) > 0: arrnd.append(a)
            a = list()
        else: a.append(array[i])
    arrnd.append(a)
    return arrnd


L = 50           # Aresta da rede
STEPS = 1000              # Número de MCS
RND = 1                 # Condição inicial dos spins
IMG = 0                 # Gravar estados
CI  = 0                 # Gravar condição inicial
TI = 2.                  # Temperatura Inicial
TF = 2.5                  # Temperatura Final
dT = 0.05                # Delta da temperatura
TRANS = 1000           # Final do Transiente 
CR = 0                 # Numero de medidas de Correlação espacial

# PLOTAR OS CLUSTERS
vis = True

hksis = np.loadtxt(sys.argv[1]+f'HK-L-{L}-TI-{TI:.2f}-TF-{TF:.2f}-dT-{dT:.2f}-STEPS-{STEPS}-RND-{RND}-TRANS-{TRANS}.dat', unpack=True)
if vis: sis = np.loadtxt(sys.argv[1]+f'snap-L-{L}-TI-{TI:.2f}-TF-{TF:.2f}-dT-{dT:.2f}-STEPS-{STEPS}-RND-{RND}-TRANS-{TRANS}.dat', unpack=True)
if vis: cls = np.loadtxt(sys.argv[1]+ f'CLS-L-{L}-TI-{TI:.2f}-TF-{TF:.2f}-dT-{dT:.2f}-STEPS-{STEPS}-RND-{RND}-TRANS-{TRANS}.dat', unpack=True)

#print(sis)
#print(cls)

hg = list()
for i in range(len(hksis)):
    if hksis[i] < 0: hg.append(-hksis[i])  
#print(hg)


t = np.arange(TI, TF+dT, dT)

plt.figure()
plt.plot(t, hg, marker='*')
plt.xlabel('T')
plt.ylabel(r'$H_{g}$')
plt.title(f'Domain-size Heterogeneity\nL = {L}')
plt.savefig(sys.argv[1]+'hg.png', dpi=400)

if(vis):
    hksis = np.asarray(split(hksis))
    sis = np.asarray(split0(sis, -2))

    vmax = max(hksis[0])
    vmin = 0
    
    hksis = np.asarray(hksis[-1].reshape((L, L)), dtype='int16')
    sis = np.asarray(sis[-1].reshape((L, L)), dtype='int16')
    
    fig, axes= plt.subplots(1, 2, figsize=(8, 4), layout='constrained')
    
    im0 = axes[0].imshow(hksis, origin='upper', vmin=0, vmax=vmax)
    axes[0].invert_xaxis()
    
    im1 = axes[1].imshow(sis, origin='upper', vmin=-1, vmax=1)
    axes[1].invert_xaxis()
    
    #for (i, j), label in np.ndenumerate(hksis):
    #    axes[0].text(j, i, label, ha='center', va='center')
    
    plt.colorbar(im0, ax=axes[0])
    plt.colorbar(im1, ax=axes[1])
    plt.savefig(sys.argv[1]+'clusters.png', dpi=400)

