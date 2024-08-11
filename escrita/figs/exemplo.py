import numpy as np
import matplotlib.pyplot as plt
import glob
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 12})

L = 5

sis1 = np.array([[1, 1, 1, 1, 1],
                 [1, 1, 0, 1, 1],
                 [1, 0, 0, 0, 1],
                 [1, 1, 0, 1, 1],
                 [1, 1, 1, 1, 1]])
sis2 = np.array([[0, 1, 1, 1, 0],
                 [1, 0, 1, 0, 1],
                 [1, 1, 0, 1, 1],
                 [1, 0, 1, 0, 1],
                 [0, 1, 1, 1, 0]])

fig, ax = plt.subplots(1, 2, figsize=(10, 5), layout='constrained')

plt.subplot(121)
plt.imshow(sis1, cmap='gray', vmax=1)
plt.xticks([], [])
plt.yticks([], [])
#plt.axis('off')

plt.subplot(122)
plt.imshow(sis2, cmap='gray', vmax=1)
plt.xticks([], [])
plt.yticks([], [])
#plt.axis('off')



plt.savefig('mini-dominios.png', dpi=500)





