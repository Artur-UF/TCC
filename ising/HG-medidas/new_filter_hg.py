import os
import fnmatch

L = 160

path = f'samples_L_{L}'
samples = fnmatch.filter(list(i.name for i in os.scandir(path)), 'HK*')
#print(samples)

c = 0
ttemp = 0
T = []
H = []

for file in samples:
    with open(os.path.join(path, file), 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.split()[0] == '#':
                ttemp = float(line.split()[2])
                if ttemp not in T:
                    T.append(ttemp)
                    H.append(float(line.split()[1]))
                    c += 1
                else:
                    H[T.index(ttemp)] += float(line.split()[1])
                    c += 1
c /= len(T)
H = list(H[k]/c for k in range(len(T)))

H = [::-1]
T = T[::-1]

with open(f'Hg_L_{L}.dat', 'w') as f:
    for i in range(len(H)):
        f.write(f'{H[i]} {T[i]}\n')

