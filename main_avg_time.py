import sys
from encrypt import Encrypt
from decrypt import Descrypt
from gensafeprime import safe_prime_generator
from genprime import prime_generator
from makesafekey import makeSafeKey
from time import time
import numpy as np

def calAverageTime():
    fi = open("Data/Time.txt","r", encoding='utf-8')
    data = []
    while fi:
        line = fi.readline()
        if line == "":
            break
        time = float(line.rstrip('\n'))
        data.append(time)
    print(data)
    print(np.mean(data))
    fi.close()

if (__name__ == "__main__"):
    fo = open("Data/Time.txt","w", encoding='utf-8')
    for i in range(0,1000):
        start_time = time()
        prime_generator(int(1024))
        makeSafeKey()
        Encrypt()
        Descrypt()
        end_time = time()
        print('Time generating: %s' %(end_time - start_time))
        fo.write(str(end_time - start_time)+'\n')
    fo.close()
    # calAverageTime()