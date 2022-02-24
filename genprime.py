import random
import PrimeTest

def Random(bits):
	a = random.getrandbits(bits)
	a = a | (1 << (bits-1))
	a = a | 1
	return a;

def getPrime(bits):
	p = Random(bits)
	d1 = d2 = d3 = 0
	while True:
		d1+= 1
		if PrimeTest.Preprocessor(p) == False:
			p+= 2
			continue
		d2+=1
		if PrimeTest.Fermat(p,20) == False:
			p+= 2
			continue
		d3+=1
		if PrimeTest.Miller_Rabin(p,20) == False:
			p+= 2
			continue
		break
	return p

def prime_generator(bits):
	p = getPrime(bits)
	q = getPrime(bits)
	fo = open("Data/BigPrime.txt","w")
	fo.write(str(p)+'\n')
	fo.write(str(q))
	fo.close()