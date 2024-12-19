import matplotlib.pyplot as plt
import numpy as np
from glob import glob
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 20})

files = glob('hh*')


marker = ['>', '^', 's', '+']
color = ['r', 'b', 'g', 'purple']

plt.figure(1, figsize=(10, 10), layout='constrained')

for i in range(len(files)):
    t, hh = np.loadtxt(files[i], unpack=True)
    plt.plot(t, hh, marker=marker[i], color=color[i], label=rf'$L = {int(files[i].split('_')[1])}$')
plt.xlabel(r'$T$')
plt.ylabel(r'$H_{hull}$')

plt.savefig('fig-hh.png', dpi=400)


