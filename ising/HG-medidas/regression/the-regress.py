import numpy as np
import glob
import scipy.optimize as opt
import matplotlib.pyplot as plt
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 15})

log = True
trans = 3 # 1 = Tc | 2 = Tc3 | 3 = Guess
points_unfitted = 3


paths = glob.glob('results*')

arks = list(np.loadtxt(i, unpack=True) for i in paths)

Ls, peaks0, hgs = np.loadtxt('results-regress.dat', unpack=True)

Li, pi = Ls[-1], peaks0[-1]

Ls = Ls[:-1]
peaks0 = peaks0[:-1]


if trans == 1:
    tc = 2.269185 # Tc da transição térmica
if trans == 2:
    tc = 2.567 # transição dependente de 3 ordem
if trans == 3:
    tc = 2.4

if log:
    if trans == 3:
        def func_fit(x, a, b, c):
            return a + b*x**c
        pr, pcov = opt.curve_fit(func_fit, 1/Ls[points_unfitted:], peaks0[points_unfitted:], p0=[tc, 1, -1])
        tc = pr[0]
        # Pontos para o scatter
        peaks = np.log10(peaks0-tc)
        Ls = np.log10(1/Ls)

        # Curva fitada
        x = np.linspace(Ls[0], Ls[-1]-0.3, 100)
        y = np.log10(pr[1]) - pr[2]*x
    else:
        def func_fit(x, b, c):
            return b/(x**c)
        pr, pcov = opt.curve_fit(func_fit, 1/Ls[points_unfitted:], peaks0[points_unfitted:]-tc)

        # Pontos para o scatter
        peaks = np.log10(peaks0-tc)
        Ls = np.log10(1/Ls)

        # Curva fitada
        x = np.linspace(Ls[0], Ls[-1]-0.3, 100)
        y = np.log10(pr[0]) - pr[1]*x
else:
    def func_fit(x, b, c):
        return b/(x**c)
    pr, pcov = opt.curve_fit(func_fit, 1/Ls, peaks0-tc)
    peaks = peaks0-tc
    Ls = 1/Ls
    x = np.linspace(0, 0.0011, 100)
    y = func_fit(x, pr[0], pr[1])


fig, ax = plt.subplots(1, 1, figsize=(8, 8), layout='constrained')
plt.subplot(111)

plt.plot(Ls, peaks, 'r', zorder=3)
plt.scatter(Ls, peaks, c='k', s=7, zorder=4)
plt.scatter([np.log10(1/Li)], [np.log10(pi-tc)], c='k', s=10, marker='*', zorder=4)

if log:
    plt.plot(x, y, 'b')

    plt.xlabel(r'$\log{(1/L)}$')
    plt.ylabel(r'$\log{[T_{*}(L)-T_c]}$')
else:
    plt.plot(x, y, 'b')

    plt.xlabel(r'$1/L$')
    plt.ylabel(r'$T_*(L)-T_c$')

plt.grid()

if trans == 1:
    plt.title(fr'$T_*(L) = {tc:.3f} + {pr[0]:.2f}/L^{pr[1]:.2f}$')
    plt.savefig('extrapolation-Tc.png', dpi=400)
if trans == 2:
    plt.title(fr'$T_*(L) = {tc:.3f} + {pr[0]:.2f}/L^{pr[1]:.2f}$')
    plt.savefig('extrapolation-Tc-new.png', dpi=400)
if trans == 3:
    plt.title(fr'$T_*(L) = {tc:.3f} + {pr[1]:.2f}/L^{pr[2]:.2f}$')
    plt.savefig('extrapolation-Tc-guess.png', dpi=400)

