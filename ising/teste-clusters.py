import numpy as np
import matplotlib.pyplot as plt
import sys


L = 15           # Aresta da rede
STEPS = 100              # Número de MCS
RND = 1                 # Condição inicial dos spins
IMG = 0                 # Gravar estados
CI  = 1                 # Gravar condição inicial
TI = 2.                  # Temperatura Inicial
TF = 2.                  # Temperatura Final
dT = 0.05                # Delta da temperatura
TRANS = 1           # Final do Transiente 
CR = 0                 # Numero de medidas de Correlação espacial

hksis = np.loadtxt(sys.argv[1]+f'HK-L-{L}-TI-{TI:.2f}-TF-{TF:.2f}-dT-{dT:.2f}-STEPS-{STEPS}-RND-{RND}-TRANS-{TRANS}.dat', unpack=True)
sis = np.loadtxt(sys.argv[1]+  f'ci-L-{L}-TI-{TI:.2f}-TF-{TF:.2f}-dT-{dT:.2f}-STEPS-{STEPS}-RND-{RND}-TRANS-{TRANS}.dat', unpack=True)

vmax = max(hksis)
vmin = 0

#hksis = np.arange(0, 225)

hksis = np.asarray(hksis[:-1].reshape((15, 15)), dtype='int16')
sis = np.asarray(sis.reshape((15, 15)), dtype='int16')

print(hksis)
print(sis)

fig, axes= plt.subplots(2, 1, figsize=(4, 8), layout='constrained')

im0 = axes[0].imshow(hksis, origin='upper', vmin=0, vmax=vmax)
im1 = axes[1].imshow(sis, origin='upper', vmin=-1, vmax=1)
for (i, j), label in np.ndenumerate(hksis):
#    print(f'({j},{i}) {label}')
    axes[0].text(i, j, label, ha='center', va='center')

plt.colorbar(im0, ax=axes[0])
plt.colorbar(im1, ax=axes[1])
plt.savefig(sys.argv[1]+'clusters.png', dpi=400)


