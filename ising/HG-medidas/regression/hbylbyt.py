import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 40})

Ls, Ts, Hs = np.loadtxt('results-regress.dat', unpack=True, dtype=np.str_)
Ls1 = np.log10(list(float(i.lstrip('0')) for i in Ls))
Hs = np.log10(list(float(i) for i in Hs))
Ls2 = list(1/float(i.lstrip('0')) for i in Ls)
Ts = np.asarray(list(float(i) for i in Ts))

tc = 2.269
t3 = 2.567

plt.figure(1, figsize=(12, 9), layout='constrained')

def func1(x, a, b):
    return a*x + b

plt.plot(Ls1, Hs, c='k', markersize=20, marker='*', linestyle='dashed')
pr, pcov = opt.curve_fit(func1, Ls1, Hs)
x = np.linspace(3.1, 3.35, 200)
plt.plot(x, func1(x, 0.98, -0.04), c='g', linestyle='solid', label=rf'Ising', zorder=0)
plt.plot(x, func1(x, 0.97, -0.065), c='b', linestyle='solid', label=rf'Percolação', zorder=0)

plt.legend(fontsize=25)
plt.ylabel(r'$\log H^*$')
plt.xlabel(r'$\log L$')
plt.yticks([2.9, 3.1, 3.3], [2.9, 3.1, 3.3])
plt.xticks([3, 3.3, 3.6], [3, 3.3, 3.6])

plt.savefig('hxl.png', dpi=400)



#------------------------------- SEGUNDA FIGURA --------------------------------------------------



fig, ax = plt.subplots(1, 2, figsize=(18, 9), layout='constrained')

xup = -2.8
xdo = -5.5


def func2(x, a, b):
    return t3 + a*x**(b)


#def func3(x, a, b):
#    return tc + a*x**(b)
b = 0.506
def func3(x, a):
    return tc + a*x**(b)



def func4(x, a, b, c):
    return c + a*x**(b)

cut = 5

pr1, pcov1 = opt.curve_fit(func2, Ls2[cut:], Ts[cut:])
pr2, pcov2 = opt.curve_fit(func3, Ls2[cut:], Ts[cut:])
pr3, pcov3 = opt.curve_fit(func4, Ls2[cut:], Ts[cut:])


print(np.sqrt(np.diag(pcov1)))
print(np.sqrt(np.diag(pcov2)))
print(np.sqrt(np.diag(pcov3)))

plt.subplot(121)
plt.scatter(np.log10(Ls2), Ts, c='k', s=300, marker='*')
x = np.linspace(10**(-4.5), 10**(-2.95), 200)

plt.plot(np.log10(x), func4(x, pr3[0], pr3[1], pr3[2]), c='k', linestyle='dashed', zorder=0, label=rf'$T_? = {pr3[2]:.2f} \> | \> a = {pr3[0]:.2f} \> | \> b = {pr3[1]:.2f}$')

plt.plot(np.log10(x), func2(x, pr1[0], pr1[1]), c='r', linestyle='dashed', zorder=0, label=rf'$T_3 = {t3:.2f} \> | \> a = {pr1[0]:.2f} \> | \> b = {pr1[1]:.2f}$')

#plt.plot(np.log10(x), func3(x, pr2[0], pr2[1]), c='g', linestyle='dashed', zorder=0, label=rf'$T_c = {tc:.2f} \> | \> a = {pr2[0]:.2f} \> | \> b = {pr2[1]:.2f}$')
plt.plot(np.log10(x), func3(x, pr2[0]), c='g', linestyle='dashed', zorder=0, label=rf'$T_c = {tc:.2f} \> | \> a = {pr2[0]:.2f} \> | \> b = {b:.2f}$')



plt.yticks([4, 3, t3, tc, 2], [4, 3, r'$T_3$', r'$T_c$', 2])
plt.xticks([-5, -4, -3], [-5, -4, -3])
plt.hlines([t3, tc], xdo, xup, colors=['r', 'g'], linestyles='dashed')
plt.xlim(xdo, xup)
plt.ylim(2, 4.3)
plt.ylabel(r'$T^*$')
plt.xlabel(r'$\log 1/L$')
plt.legend(loc='upper left', fontsize=23)

plt.text(-5.4, 3.5, '(a)')
ax[0].annotate(r'$L=3500$', xy=(np.log10(Ls2)[-1], Ts[-1]), xycoords='data', xytext=(-5, 3.5), textcoords='data', va='top', ha='left',
               fontsize=20, arrowprops=dict(facecolor='black', width=1.))

#plt.savefig('txl.png', dpi=400)

#plt.figure(3, figsize=(10, 10), layout='constrained')

plt.subplot(122)

# Com 3 parametros fitados

#def func2(x, a, b, c):
#    return c + a*x**(b)
#
#cut = 3
#
#pr, pcov = opt.curve_fit(func2, Ls2[cut:], Ts[cut:])


plt.scatter(np.log10(Ls2), np.log10(Ts - pr3[2]), c='k', s=300, marker='*')



xlim = (-4.2, -2.95)
ylim = (-0.7, 0.3)

x0 = np.linspace(10**(xlim[0]), 10**(xlim[1]), 200)

# Com 2 parametros fitados
#def func2(x, a, b):
#    return a - b*x

#def func3(x, a, b):
#    return a - b*x


X3 = np.log10(Ls2)
T3 = np.log10(Ts - t3)
TC = np.log10(Ts - tc)


#xlim = (-4.2, -2.9)
#ylim = (-0.57, 0.33)


#pr3, pcov3 = opt.curve_fit(func2, X3[cut:], T3[cut:])
#pr4, pcov4 = opt.curve_fit(func3, X3[cut:], TC[cut:])



plt.scatter(X3, T3, c='r', s=300, marker='*')
plt.scatter(X3, TC, c='g', s=300, marker='*')
x = np.linspace(10**(xlim[0]), 10**(xlim[1]), 200)

#plt.plot(np.log10(x0), (np.log10(pr2[0]) + abs(pr2[1])*np.log10(x0)), c='g', linestyle='dashed', zorder=0, label=rf'$T_c = {tc:.2f} \> | \> a = {pr2[0]:.2f} \> | \> b = {pr2[1]:.2f}$')
plt.plot(np.log10(x0), (np.log10(pr2[0]) + (b)*np.log10(x0)), c='g', linestyle='dashed', zorder=0, label=rf'$T_c = {tc:.2f} \> | \> a = {pr2[0]:.2f} \> | \> b = {b:.2f} $')

plt.plot(np.log10(x0), (np.log10(pr1[0]) + abs(pr1[1])*np.log10(x0)), c='r', linestyle='dashed', zorder=0, label=rf'$T_3 = {t3:.2f} \> | \> a = {pr1[0]:.2f} \> | \> b = {pr1[1]:.2f}$')

plt.plot(np.log10(x0), (np.log10(pr3[0]) + abs(pr3[1])*np.log10(x0)), c='k', linestyle='dashed', zorder=0, label=rf'$T_? = {pr3[2]:.2f} \> | \> a = {pr3[0]:.2f} \> | \> b = {abs(pr3[1]):.2f}$')


plt.yticks([-0.6, -0.4, -0.2, 0.0, 0.2], [-0.6, -0.4, -0.2, 0.0, 0.2])
plt.xticks([-4, -3.5, -3], [-4, -3.5, -3])
plt.xlim(xlim[0], xlim[1])
plt.ylim(ylim[0], ylim[1])
plt.ylabel(r'$\log (T^*-T_?)$', labelpad=14)
plt.xlabel(r'$\log 1/L$')
plt.legend(loc='lower right', fontsize=23)

plt.text(-4.15, -0.05, '(b)')

plt.savefig('txl-all-tc-bising.png', dpi=400)



