import numpy as np
import matplotlib.pyplot as plt
import glob
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 12})

L = 500
Nf = 5
TI = 1
TF = 5
dT = 1

path = 'snapshot'

path_snap = glob.glob(path+'/snap*')[0]
path_hk = glob.glob(path+'/HK*')[0]

sis = np.loadtxt(path_snap, unpack=True)

sis = sis.reshape((Nf, L**2+1))

fig, ax = plt.subplots(1, Nf, figsize=(10, 2), layout='constrained')

for i in range(Nf):
    formato = 100+(Nf*10)+1+i
    plt.subplot(formato)
    snap = sis[i][:-1].reshape((L, L))
    plt.imshow(snap, cmap='gray', vmax=1)
    plt.axis('off')
    plt.title(f'T = {TI+(i*dT):.1f}')
plt.savefig(path+f'/imgs/all-img{L}.png', dpi=500)





