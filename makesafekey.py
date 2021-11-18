import MyMath
import genprime
import random

def getPQ(file):
	fi = open(file,"r")
	p = int(fi.readline())
	q = int(fi.readline())
	return p, q

def getD(phi, n):
	d = random.getrandbits(n)
	d = d | (1 << (round(n/4)-1))
	d = d | 1
	# d = GenePrime.Random(n)
	while True:
		if MyMath.GCD(d,phi) == 1:
			break
		d+= 2
	return d

def getE(d, phi):
	e = MyMath.GCD_extended(d,phi)[0] #[x,y,z] #d = x
	if e < 0:
		e+= phi
	return e

def main():
	p, q = getPQ("Data/BigPrime.txt")
	n = p*q
	phi = (p-1)*(q-1)
	# e = getE(phi)
	# d = getD(e, phi)
	d = getD(phi, int(len(bin(p)))-2)
	e = getE(d, phi)
	fo = open("Data/PublicKey.txt","w")
	fo.write(str(n)+'\n'+str(e))
	fo.close()
	fo = open("Data/PrivateKey.txt","w")
	fo.write(str(n)+'\n'+str(d))
	fo.close()

main()