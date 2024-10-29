import numpy as np
from glob import glob


path = 'teste-cls'
samples = glob(path+'/CLS*')

info = open(path+'/info.txt', 'r')
nfiles = info.readlines()[11].split(' ')[1]
print(int(nfiles))





