from glob import glob

L = 50
path = f'mag_{L}'
samples = glob(path+'/medidas*')

M = []
T = []
Tcount = []

for j in range(len(samples)):
    with open(samples[j], 'r') as f:
        line = f.readline()
        while line != '':
            if line.split(' ')[0] == '#':
                ttemp = float(line.split(' ')[1])
                if ttemp not in T:
                    T.append(ttemp)
                    Tcount.append(0)
                    M.append(0)
            else:
                M[T.index(ttemp)] += abs(float(line.split(' ')[1]))
                Tcount[T.index(ttemp)] += 1

            line = f.readline()

M = list(M[i]/Tcount[i] for i in range(len(M)))
M = M[::-1]
T = T[::-1]

with open(f'mag-{L}-results.dat', 'w') as f:
    for i in range(len(M)):
        f.write(f'{T[i]} {M[i]}\n')


