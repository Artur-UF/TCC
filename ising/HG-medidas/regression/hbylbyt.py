import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 40})

Ls, Ts, Hs = np.loadtxt('results-regress.dat', unpack=True, dtype=np.str_)
Ls1 = np.log10(list(float(i.lstrip('0')) for i in Ls))
Hs = np.log10(list(float(i) for i in Hs))
Ls2 = list(1/float(i.lstrip('0')) for i in Ls)
Ts = list(float(i) for i in Ts)

tc = 2.269
t3 = 2.567

fig, ax = plt.subplots(1, 2, figsize=(20, 10), layout='constrained')

plt.subplot(121)
def func1(x, a, b):
    return a*x + b

plt.scatter(Ls1, Hs, c='k', s=300, marker='*')
pr, pcov = opt.curve_fit(func1, Ls1, Hs)
x = np.linspace(Ls1[0], Ls1[-1], 500)
plt.plot(x, func1(x, pr[0], pr[1]), c='gray', linestyle='dashed', label=rf'$f(L) = ({pr[0]:.2f})L {pr[1]:.2f}$', zorder=0)

plt.ylabel(r'$\log H^*$')
plt.xlabel(r'$\log L$')
plt.yticks([2.9, 3.1, 3.3], [2.9, 3.1, 3.3])
plt.xticks([3, 3.3, 3.6], [3, 3.3, 3.6])


plt.subplot(122)
xup = -2.8
xdo = -7



def func2(x, a, b):
    return t3 + a*x**(b)

def func3(x, a, b):
    return tc + a*x**(b)


pr1, pcov1 = opt.curve_fit(func2, Ls2, Ts)
pr2, pcov2 = opt.curve_fit(func3, Ls2, Ts)


plt.scatter(np.log10(Ls2), Ts, c='k', s=300, marker='*')
x = np.linspace(10**(-4.5), 10**(-2.9), 200)
plt.plot(np.log10(x), func2(x, pr1[0], pr1[1]), c='r', linestyle='dashed', zorder=0)
plt.plot(np.log10(x), func3(x, pr2[0], pr2[1]), c='g', linestyle='dashed', zorder=0)

plt.yticks([4.2, 3.2, t3, tc, 2], [4.2, 3.2, r'$T_3$', r'$T_c$', 2])
plt.xticks([-7, -6, -5, -4, -3], [-7, -6, -5, -4, -3])
plt.hlines([t3, tc], xdo, xup, colors=['r', 'g'], linestyles='dashed')
plt.xlim(xdo, xup)
plt.ylabel(r'$T^*$')
plt.xlabel(r'$\log 1/L$')

plt.savefig('hxlxt.png', dpi=400)


