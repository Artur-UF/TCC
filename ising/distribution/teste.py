import numpy as np
import matplotlib.pyplot as plt


L = 500**2
n = 200


linbins = np.arange(0, L)
logbins = np.logspace(np.log10(1), np.log10(L), n)

r = logbins[1]/logbins[0]

print(logbins)
print(r)
print(f'{logbins[0]*r}, {logbins[0]*r**2}, {logbins[0]*r**3}')

