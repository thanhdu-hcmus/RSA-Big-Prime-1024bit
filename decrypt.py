import MyMath
import MyBase
import makesafekey
import PrimeTest

def getPrivateKey (file) : # file Privatekey
	fi = open(file,"r", encoding='utf-8')
	n = int(fi.readline())
	d = int(fi.readline())
	fi.close()
	return n, d

def getCiphertext(file): # file Ciphertext
	fi = open(file,"r", encoding='utf-8')
	C = fi.readline()
	C = C.split(" ")
	C = C[:-1]
	fi.close()
	return C

def decryptFast(c,d,n):
	p, q = makesafekey.getPQ("Data/BigPrime.txt")
	d1 = d % (p-1)
	d2 = d % (q-1)
	c1 = MyMath.powMod(c, d1, p)
	c2 = MyMath.powMod(c, d2, q)
	return MyMath.CRT(p,c1,q,c2)

def decode(n, d, C, base, fileOut): # file PlanintextDecode
	fo = open(fileOut,"w", encoding='utf-8')
	P = ""
	for i in C:
		# m = MyMath.powMod(MyBase.toInt(i,64),d,n)
		m = decryptFast(MyBase.toInt(i,64),d,n)
		c = str(m)
		while len(c) % base != 0:
			c = '0' + c
		x = 0
		while x != len(c):
			a = c[x:x+base]
			x+= base
			P+= chr(int(a))
			fo.write(chr(int(a)))
	fo.close()
	return P

def Descrypt():
	n, d= getPrivateKey("Data/PrivateKey.txt")
	C= getCiphertext("Data/Ciphertext.txt")
	C= decode(n, d, C, 4, "Data/PlaintextDecode.txt")
	#print(C)