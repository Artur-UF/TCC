import numpy as np
import glob
import scipy.stats as sp
import matplotlib.pyplot as plt
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 12})

log = False
trans = True

paths = glob.glob('results*')

arks = list(np.loadtxt(i, unpack=True) for i in paths)

peaks = (arks[0][1] + arks[1][1])/2

Ls = arks[0][0]


if trans:
    tc = 2.69185 # Tc da transição térmica 
else:
    tc = 2.567 # transição dependente de 3 ordem


if log:
    peaks = np.log10(peaks-tc)
    Ls = np.log10(1/Ls)
else:
    peaks = peaks-tc
    Ls = 1/Ls


def func(x, a, b):
    return a*x + b


fig, ax = plt.subplots(1, 1, figsize=(8, 8), layout='constrained')
plt.subplot(111)

plt.plot(Ls, peaks, 'r')
plt.scatter(Ls, peaks, c='k', s=7, zorder=3)

pr = sp.linregress(Ls, peaks)
x = np.linspace(0, 0.0011 ,100)
y = func(x, pr[0], pr[1])

plt.plot(x, y, 'b')

if log:
    plt.xlabel(r'$\log{(1/L)}$')
    plt.ylabel(r'$\log{[T_{*}(L)-T_c]}$')
else:
    plt.xlabel(r'$1/L$')
    plt.ylabel(r'$T_*(L)-T_c$')

plt.grid()
#plt.show()
plt.savefig('extrapolation.png', dpi=400)

