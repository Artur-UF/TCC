import numpy as np
import scipy.optimize as sp
import matplotlib.pyplot as plt
import glob
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 12})


paths = glob.glob('full-dense*')
paths = sorted(paths)

hg = list(np.loadtxt(i, unpack=True) for i in paths)

def func(x, a, b, c, d):
    return a*x**3 + b*x**2 + c*x + d

# RESULTS FILE
f = open(f'results-regress.dat', 'w+')
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-


fig, ax = plt.subplots(1, 1, figsize=(8, 8), layout='constrained')

plt.subplot(111)
for i in range(len(paths)):
    L = paths[i].split("-")[3].split(".")[0]
    plt.scatter(hg[i][1], hg[i][0], s=7, label=f'L = {L}')
    x = np.linspace(hg[i][1][0], hg[i][1][-1], 1000)

    pr, pcov = sp.curve_fit(func, hg[i][1][:], hg[i][0][:])

    xy = [list(x), list(func(x, *pr))]

    yv = max(func(x, *pr))
    xv = xy[0][xy[1].index(yv)]

    #xv = -pr[1]/(2*pr[0])

    f.write(f'{L} {xv} {func(xv, *pr)}\n')

    plt.vlines(xv, 650, yv, 'k')

    plt.plot(x, func(x, *pr))

f.close()
plt.xlabel('T')
plt.ylabel(r'$H_{g}$')
plt.legend()
plt.grid()
plt.savefig('preliminar-fit.png', dpi=400)

