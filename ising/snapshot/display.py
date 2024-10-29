import numpy as np
import matplotlib.pyplot as plt
import glob
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 30})

L = 500 
TI = 1
TF = 5
dT = .5

Nf = len(np.arange(TI, TF+dT, dT))

path = 'snapshot'

path_12 = glob.glob(path+'/snap_L_500_TI_1.00*')[0]
path_tc = glob.glob(path+'/snap_L_500_TI_2.27*')[0]
path_10 = glob.glob(path+'/snap_L_500_TI_10.00*')[0]

sis_12 = np.loadtxt(path_12, unpack=True)
sis_tc = np.loadtxt(path_tc, unpack=True)
sis_10 = np.loadtxt(path_10, unpack=True)

sis_12 = sis_12.reshape((2, L**2+1))

sis = np.asarray([sis_12[0], sis_12[1], sis_tc, sis_10])

T = [1.00, 2.00, 2.269, 10.00]

fig, ax = plt.subplots(1, 4, figsize=(15, 4), layout='constrained')

for i in range(4):
    formato = 140+1+i
    plt.subplot(formato)
    snap = sis[i][:-1].reshape((L, L))
    plt.imshow(snap, cmap='gray', vmax=1)
    plt.title(f'T = {T[i]:.2f}')
    plt.xticks([], [])   
    plt.yticks([], [])
plt.savefig(path+f'/imgs/all-img{L}.png', dpi=500)
#plt.subplot(111)
#snap = sis[4][:-1].reshape((L, L))
#plt.imshow(snap, cmap='gray', vmax=1)
#plt.xticks([], [])
#plt.yticks([], [])
#plt.title(r'$T = 2.5$')
#plt.savefig(path+f'/imgs/small-ex{L}.png', dpi=500)





