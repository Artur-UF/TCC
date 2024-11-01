import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 40})

Ls, Ts, Hs = np.loadtxt('results-regress.dat', unpack=True, dtype=np.str_)
Ls = list(1/float(i.lstrip('0')) for i in Ls)
Ts = list(float(i) for i in Ts)


fig, ax = plt.subplots(1, 1, figsize=(10, 10), layout='constrained')

def func(x, a, b, c):
    return a + b*x**(c)

pr, pcov = opt.curve_fit(func, Ls, Ts)

plt.scatter(np.log10(Ls), Ts, c='k', s=150, marker='*')
x = np.linspace(10**(-4.5), 10**(-3), 200)
plt.plot(np.log10(x), func(x, pr[0], pr[1], pr[2]), c='gray', linestyle='dashed', zorder=0)

plt.yticks([4.2, 3.2, 2.567, 2.269, 1.2], [4.2, 3.2, r'$T_3$', r'$T_c$', 1.2])
plt.xticks([-7, -6, -5, -4, -3], [-7, -6, -5, -4, -3])
plt.ylabel(r'$T^*$')
plt.xlabel(r'$\log 1/L$')


plt.savefig('hxt.png', dpi=400)

