import numpy as np
import matplotlib.pyplot as plt
import sys


L = 50           # Aresta da rede
STEPS = 100              # Número de MCS
RND = 1                 # Condição inicial dos spins
IMG = 0                 # Gravar estados
CI  = 0                 # Gravar condição inicial
TI = 2.                  # Temperatura Inicial
TF = 2.                  # Temperatura Final
dT = 0.05                # Delta da temperatura
TRANS = 1           # Final do Transiente 
CR = 0                 # Numero de medidas de Correlação espacial

hksis = np.loadtxt(sys.argv[1]+f'HK-L-{L}-TI-{TI:.2f}-TF-{TF:.2f}-dT-{dT:.2f}-STEPS-{STEPS}-RND-{RND}-TRANS-{TRANS}.dat', unpack=True)
sis = np.loadtxt(sys.argv[1]+f'snap-L-{L}-TI-{TI:.2f}-TF-{TF:.2f}-dT-{dT:.2f}-STEPS-{STEPS}-RND-{RND}-TRANS-{TRANS}.dat', unpack=True)
cls = np.loadtxt(sys.argv[1]+ f'CLS-L-{L}-TI-{TI:.2f}-TF-{TF:.2f}-dT-{dT:.2f}-STEPS-{STEPS}-RND-{RND}-TRANS-{TRANS}.dat', unpack=True)

print(sis)
print(cls)

vmax = max(hksis)
vmin = 0

hksis = np.asarray(hksis[:-1].reshape((L, L)), dtype='int16')
sis = np.asarray(sis.reshape((L, L)), dtype='int16')

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


