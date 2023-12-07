#!/usr/bin/python3
import matplotlib.pyplot as plt
import sys
import numpy as np

plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 12})

t, en, mag, corrt = np.loadtxt(sys.argv[1]+'medidas_L_100_TI_2.27_TF_2.27_dT_0.50_STEPS_100000_RND_1_TRANS_1_1701032807.dat', unpack=True)

t, en, mag, corrt = t[:-1], en[:-1], mag[:-1], corrt[:-1]

plt.subplots(layout='constrained', figsize=(8, 4))
plt.axis('off')

plt.subplot(121)
plt.plot(t, en, 'r', linewidth=1, label=r'$L = 100$')
plt.xlabel('t(MCS)')
plt.ylabel('E/N')
plt.xscale('log')
plt.grid()
plt.legend()

plt.subplot(122)
plt.plot(t, mag, 'r', linewidth=1, label=r'$L = 100$')
plt.xlabel('t(MCS)')
plt.ylabel('m')
plt.xscale('log')
plt.grid()
plt.legend()

plt.savefig(sys.argv[1]+'plot.png', dpi=400)

