from math import nan
import random
import PrimeTest
from MyMath import powMod, GCD
from time import sleep

def Random (bits):
	a = random.getrandbits(bits)
	a = a | (1 << (bits-1))
	a = a | 1
	return a

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)/2
    return random.randint(range_start, range_end)

def getPrimeWithNDigits(n):
	while True:
		p = random_with_N_digits(n)
		if PrimeTest.Preprocessor(p) == False:
			continue
		if PrimeTest.Fermat(p,20) == False:
			continue
		if PrimeTest.Miller_Rabin(p,20) == False:
			continue
		break
	return p

def findSafePrimeAlgo():
	p1 = getPrimeWithNDigits(10)
	startRange = 2*(p1+1)
	print("Start Range:", startRange)
	d1 = int(len(str(p1)))
	endRange = 10**(d1-1)
	print("End Range:", endRange)
	for k in range(startRange-1, endRange-1, -1):
		p2 = 2*k*p1 + 1
		d2 = int(len(str(p2)))
		if d2 != 2*d1:
			continue
		elif d2 < 2*d1:
			break
		print("++++++++++++++++++")
		print("k:", k)
		print("p2:", p2)
		print("p1:", p1)
		print("++++++++++++++++++")
		print("===============")
		print("d2:", d2)
		print("d1:", d1)
		print("===============")
		sleep(5)
		for a in range(2,p2-1,1):
			print("a:", a)
			if((powMod(a, k*p1 , p2) == p2-1) and (GCD(a**k + 1, p2) == 1)):
				return p2
	return nan

def getPrime(b):
	p = Random(b)
	while True:
		if PrimeTest.Preprocessor(p) == False:
			p+= 2
			continue
		if PrimeTest.Fermat(p,20) == False:
			p+= 2
			continue
		if PrimeTest.Miller_Rabin(p,20) == False:
			p+= 2
			continue
		break
	return p

def prime_generator(bits):
	p = getPrime(bits)
	q = getPrime(bits)
	fo = open("Data/BigPrime.txt","w", encoding='utf-8')
	fo.write(str(p)+'\n')
	fo.write(str(q))
	fo.close()

if __name__ == "__main__":
	findSafePrimeAlgo()