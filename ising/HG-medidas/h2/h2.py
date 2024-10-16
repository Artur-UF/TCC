import numpy as np
import matplotlib.pyplot as plt
import glob
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 12})

paths = sorted(glob.glob('dense*'))


fig, ax = plt.subplots(1, 1, figsize=(10, 10), layout='constrained')


markers = ['s', '^', 'v', '*', 'd', '>']

for i in range(len(paths)):
    h, h2, t = np.loadtxt(paths[i], unpack=True)
    plt.plot(t, h2, marker=markers[i], label=f'L = {int(paths[i].split('_')[-1].split('.')[0])}')

plt.vlines(2.269, 0, 3.6e+06, colors='k', linestyle='dashed', linewidth=.7)
plt.xlim(1., 10.)
plt.ylim(0., 3.6e+06)
plt.xlabel('T')
plt.ylabel(r'$H^2$')
plt.xticks([1, 2.269, 3,  4, 5, 6, 7, 8, 9, 10], [1, r'$T_{c}$', 3, 4, 5, 6, 7, 8, 9, 10])
plt.legend()
plt.savefig('plot-h2.png', dpi=400)

