import matplotlib.pyplot as plt
import numpy as np
import glob
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 15})

def log_bins(bins, D, start, end, n):  # AINDA NÃO TA PRONTO
    logbins = np.logspace(np.log10(start), np.log10(end), n)
    newD = np.zeros(n)
    k = 0
    for i in range(n):
        for j in range(k, len(logbins)):
            if bins[j] <= logbins[i]:
                newD[i] += D[j]
            if bins[j] > logbins[i]:
                k = j
                break
    return logbins, newD

path = glob.glob('distribu*')

L = int(path[0].split('-')[1].split('.')[0])

Ds = np.loadtxt(path[0], unpack=True)

fig, ax = plt.subplots(1, 1, figsize=(10, 10), layout='constrained')

for i in range(len(Ds)):
    T = Ds[i][0]
    D = Ds[i][2:]
    S = np.arange(0, len(D), 1)
    plt.plot(S, D, label=f'{T}')

plt.xscale('log')
plt.yscale('log')
plt.ylabel('Frequency')
plt.xlabel('Sizes')
plt.legend(loc='upper right')
plt.title('Distribution')


plt.savefig('dis-plot.png', dpi=400)

