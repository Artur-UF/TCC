import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sp
from glob import glob
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 20})

L = 1920

files = sorted(glob(f'hg-distri_{L}*'))


def func(x, a, b, c):
    return a*x**2 + b*x + c


fig, ax = plt.subplots(1, 2, figsize=(12, 5), layout='constrained')

plt.subplot(121)
hg, fr = np.loadtxt(files[0], unpack=True)
logfr = np.log10(fr)
plt.scatter(hg, logfr, c='r', marker='^', label=rf'$T = {float(files[0].split('_')[2])}$')

pr, pcov = sp.curve_fit(func, hg, logfr)
cut1 = 3
x = np.linspace(hg[cut1], hg[-cut1])
plt.plot(x, func(x, pr[0], pr[1], pr[2]), 'k')

plt.text(405, 3, '(a)')
plt.ylabel(r'$\log n_H$', fontsize=30)
plt.xlabel(r'$H$', fontsize=30)
plt.legend()

plt.subplot(122)
hg, fr = np.loadtxt(files[1], unpack=True)
logfr = np.log10(fr)
plt.scatter(hg, logfr, c='r', marker='^', label=rf'$T = {float(files[1].split('_')[2])}$')

pr, pcov = sp.curve_fit(func, hg, logfr)
cut2 = 3
x = np.linspace(hg[cut2], hg[-cut2])
plt.plot(x, func(x, pr[0], pr[1], pr[2]), 'k')

plt.text(1355, 3.1, '(b)')
plt.ylabel(r'$\log n_H$', fontsize=30)
plt.xlabel(r'$H$', fontsize=30)
plt.legend()

plt.suptitle(fr'$L={L}$')

plt.savefig(f'comp-hg-distri-{L}.png', dpi=400)


