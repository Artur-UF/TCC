import numpy as np
import matplotlib.pyplot as plt
from glob import glob

L = 1920 
Tp = 3.62

files = glob(f'hg-distri_{L}*')

plt.figure(1, figsize=(10, 10), layout='constrained')


hg, fr = np.loadtxt(files[0], unpack=True)

plt.plot(hg, fr, marker='^')
plt.xlabel(r'$H$')
plt.title(fr'$L={L}\; |\; T={Tp}$')

plt.savefig(f'img-hg-distri-{L}-{Tp}.png')


