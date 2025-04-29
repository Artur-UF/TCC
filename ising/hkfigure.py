import matplotlib.pyplot as plt
import numpy as np
from glob import glob
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 40})

L = 50

path = 'imgs'
sispath = glob(path+'/snap*')[0]
hkpath = glob(path+'/HK*')[0]

sis = np.reshape(np.loadtxt(sispath)[:-1], (L, L))
hk = np.loadtxt(hkpath, skiprows=1)

hkcount = []
for i in range(len(hk)):
    if hk[i] not in hkcount:
        hkcount.append(hk[i])
hkmax = max(hkcount)
hkmin = min(hkcount)
values = np.linspace(hkmin, hkmax, len(hkcount))

nhk = []
for i in range(len(hk)):
    nhk.append(values[hkcount.index(hk[i])])
nhk = np.reshape(np.asarray(nhk), (L, L))

#fig, ax = plt.subplots(1, 2, figsize=(20, 10), layout='constrained')
#
#plt.subplot(121)
#plt.imshow(sis, cmap='Greys')
#plt.xticks([],[])
#plt.yticks([],[])
#plt.title(r'$(a)$')

#for (i, j), label in np.ndenumerate(np.reshape(np.arange(0, L**2, 1), (L, L))):
#    ax[0].text(j, i, label, ha='center', va='center', fontsize=10, backgroundcolor='w')


#plt.subplot(122)
plt.figure(1, figsize=(10, 10), layout='constrained')

plt.imshow(nhk, cmap='gist_ncar', vmin=hkmin, vmax=hkmax)
plt.xticks([],[])
plt.yticks([],[])
#plt.title(r'$(b)$')

#for (i, j), label in np.ndenumerate(np.reshape(hk, (L, L))):
#    ax[1].text(j, i, int(label), ha='center', va='center', fontsize=10, backgroundcolor='w')

plt.savefig('hkimg-new.png', dpi=400)

