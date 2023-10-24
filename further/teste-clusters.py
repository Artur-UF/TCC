import numpy as np
import matplotlib.pyplot as plt
import sys


hksis = np.loadtxt(sys.argv[1]+'HK-L-15-TI-2.00-TF-2.00-dT-0.05-STEPS-1000-RND-1-TRANS-10.dat', unpack=True)
sis = np.loadtxt(sys.argv[1]+'ci-L-15-TI-2.00-TF-2.00-dT-0.05-STEPS-1000-RND-1-TRANS-10.dat', unpack=True)

vmax = max(hksis)
vmin = 0

#hksis = np.arange(0, 225)

hksis = np.asarray(hksis[:-1].reshape((15, 15)), dtype='int16')
sis = np.asarray(sis.reshape((15, 15)), dtype='int16')

print(hksis)
print(sis)

#fig = plt.figure(layout='constrained')
#plt.imshow(hksis, origin='lower', vmin=0, vmax=225)
#for (i, j), label in np.ndenumerate(hksis):
#    print(f'({j},{i}) {label}')
#    plt.text(i, j, label, ha='center', va='center')
#
#plt.colorbar()
#plt.savefig(sys.argv[1]+'clusters.png', dpi=400)


