import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
import glob
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 12})

paths = glob.glob('full-dense*')
paths = sorted(paths)

hg = list(np.loadtxt(i, unpack=True) for i in paths)

fig, ax = plt.subplots(1, 1, figsize=(8, 8), layout='constrained')

colors = ['r', 'b', 'g', 'purple', 'orange', 'pink']

def func(x, a, b):
    return a*x + b

# RESULTS FILE
f = open(f'results-grad.dat', 'w+')
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-


plt.subplot(111)
for i in range(len(paths)):
    y = np.gradient(hg[i][0], .5)
    L = paths[i].split("-")[3].split(".")[0]
    plt.plot(hg[i][1], y, linestyle='--', c=colors[i], label=f'L = {L}')

    pr = sp.linregress(hg[i][1][3:-5], y[3:-5])
    x = np.linspace(hg[i][1][3], hg[i][1][-5], 100)
    plt.plot(x, pr[0]*x + pr[1], c=colors[i])

    root = -pr[1]/pr[0]
    f.write(f'{L} {root} {func(root, pr[0], pr[1])}\n')
    plt.vlines(root, -10, 10, 'k')

f.close()
plt.xlabel('T')
plt.ylabel(r'$dH_{g}/dT$')
#plt.ylim(-10, 10)
plt.legend()
plt.grid()
#plt.show()
plt.savefig('preliminar-grad.png', dpi=400)

