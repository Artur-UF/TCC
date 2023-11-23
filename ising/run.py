import os
import sys
import random
import time

def definer(ark, *args):
    '''
    Recebe um arquvio .c e edita os #defines com os argumetos dados nessa ordem:
    PASTA, SEED, L, STEPS, RND, IMG, CI, TI, TF, dT, TRANS, CR
    '''
    with open(main, 'r') as f:
        linhas = f.readlines()
    
    params = {'PASTA':args[0],
            'SEED':f'{args[1]}',
            'L':f'{args[2]}',
            'STEPS':f'{args[3]}',
            'RND':f'{args[4]}',
            'IMG':f'{args[5]}',
            'CI':f'{args[6]}',
            'TI':f'{args[7]}',
            'TF':f'{args[8]}',
            'dT':f'{args[9]}',
            'TRANS':f'{args[10]}',
            'CR':f'{args[11]}'}
    
    with open(main, 'w') as f:
        for l in range(len(linhas)):
            var = linhas[l].split(' ')
            if var[0] == '#define':
                var[2] = params[var[1]]
            f.write(' '.join(var))

main = "ising2D.c"
PASTA = 'resultados'
SEED = int(time.time())
L = [25, 50, 75, 100]           # Aresta da rede
STEPS = 5000              # Número de MCS
RND = 0                 # Condição inicial dos spins
IMG = 0                 # Gravar estados
CI  = 0                 # Gravar condição inicial
TI = 2.                  # Temperatura Inicial
TF = 3.                  # Temperatura Final
dT = 0.05                # Delta da temperatura
TRANS = 1000           # Final do Transiente 
CR = 0                 # Numero de medidas de Correlação espacial

AM = 1                 # Número de amostras

# Cria a pasta que eu dei o nome
try:
    os.mkdir(PASTA)
except FileExistsError:
    os.system(f'rm -rf {PASTA}/*')

info = open(f'{PASTA}/info.txt', 'w')

# Realiza as amostras

print(f"L   STEPS  RND IMG CI TI   TF   dT   TRANS  CR\n")
for l in range(len(L)):
    start = time.time()
    info.write(f'***{AM} Amostra(s)***\n\n')
    info.write(f'Seed = {SEED}\n')
    info.write(f'L = {L[l]}\n')
    info.write(f'STEPS = {STEPS}\n')
    info.write(f'RND = {RND}\n')
    info.write(f'IMG = {IMG}\n')
    info.write(f'CI = {CI}\n')
    info.write(f'TI = {TI}\n')
    info.write(f'TF = {TF}\n')
    info.write(f'dT = {dT}\n')
    info.write(f'TRANS = {TRANS}\n')
    info.write(f'CR = {CR}\n')

    definer(main,  '\"resultados\"', SEED, L[l], STEPS, RND, IMG, CI, TI, TF, dT, TRANS, CR)
    
    os.system(f'gcc {main} -O3 -lm')   
    os.system(f'./a.out')
    SEED += 3
 
    info.write(f'Execution time = {time.time() - start:.4f} s\n')
    info.write('-'*35+'\n')
    print(f'{L[l]:<3d} {STEPS:<6d} {RND:<3d} {IMG:<3d} {CI:<2d} {TI:<.2f} {TF:<.2f} {dT:.2f} {TRANS:<6d} {CR:<2d}\n')
info.close()

