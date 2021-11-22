import genprime
import PrimeTest
from time import time
def getSafePrime(n):
	while True:
		t = genprime.getPrime(n-1) #1023 bits
		p = ( 2 * t ) + 1
		if PrimeTest.Preprocessor(p) == False:
			continue
		if PrimeTest.Fermat(p,20) == False:
			continue
		if PrimeTest.Miller_Rabin(p,20) == False:
			continue
		break
	return p

def safe_prime_generator(bits):
	start_time = time ()
	print("====== Start Gen======")
	p = getSafePrime(bits)
	q = getSafePrime(bits)
	fo = open("Data/BigPrime.txt","w", encoding='utf-8')
	fo.write(str(p)+'\n')
	fo.write(str(q))
	fo.close()
	end_time = time ()
	print("====== End Gen======")
	print ("Generating: {}".format(end_time - start_time)) 


if __name__ == "__main__":
	getSafePrime(1024)