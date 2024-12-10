import matplotlib.pyplot as plt
import numpy as np
from glob import glob
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 35})

L = 50

path = 'imgs'
sispath = glob(path+'/snap*')[0]
hkpath = glob(path+'/HK*')[0]

sis = np.reshape(np.loadtxt(sispath)[:-1], (50, 50))
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
nhk = np.reshape(np.asarray(nhk), (50, 50))

fig, ax = plt.subplots(1, 2, figsize=(20, 10), layout='constrained')

plt.subplot(121)
plt.imshow(sis, cmap='Greys')
plt.xticks([],[])
plt.yticks([],[])
plt.title(r'$(a)$')

plt.subplot(122)
plt.imshow(nhk, cmap='nipy_spectral', vmin=hkmin, vmax=hkmax)
plt.xticks([],[])
plt.yticks([],[])
plt.title(r'$(b)$')

plt.savefig('hkimg.png', dpi=400)

