import genprime
import PrimeTest

def getSafePrime(n):
	t = genprime.getPrime(n-1)
	p = 2*t + 1
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

def main(bits):
	p = getSafePrime(bits)
	q = getSafePrime(bits)
	fo = open("Data/BigPrime.txt","w")
	fo.write(str(p)+'\n')
	fo.write(str(q))
	fo.close()

main(1024)