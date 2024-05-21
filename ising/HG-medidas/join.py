import numpy as np

hg1, t1 = np.loadtxt('denseB-hg-1920.dat', unpack=True)
hg2, t2 = np.loadtxt('dense-hg-1920.dat', unpack=True)

f = open('full-dense-hg-1920.dat', 'w+')

n = len(t1) + len(t2)

hg1 = list(hg1) 
t1 = list(t1)

hg2 = list(hg2)
t2 = list(t2)


c = 0
switch = 1
while c < n:
    if switch > 0:
        f.write(f'{hg1.pop(0)} {t1.pop(0)}\n')
    if switch < 0:
        f.write(f'{hg2.pop(0)} {t2.pop(0)}\n')
    switch *= -1
    c += 1

f.close()

