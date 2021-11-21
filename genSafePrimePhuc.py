import libnum
import sympy
import random
import sys


from Crypto.Util.number import getPrime
from Crypto.Random import get_random_bytes



primebits=64

if (len(sys.argv)>1):
  primebits=int(sys.argv[1])

s = getPrime(primebits,randfunc=get_random_bytes)
t = getPrime(primebits,randfunc=get_random_bytes)

print (f"s={s}")
print (f"t={t}")

isPrime=False
i=random.randint(0,100)
while (isPrime==False):
  r=2*i*t+1
  i=i+1
  if (sympy.isprime(r)==True): 
    isPrime=True

print (f"r={r}")

p_0 = 2*(pow(s,r-2,r))*s-1

print (f"\np_0={p_0}")

isPrime=False
j=random.randint(0,100)
p=0
while (isPrime==False):
  p=p_0+2*j*r*s
  j=j+1
  if (sympy.isprime(p)==True): 
    isPrime=True

print (f"p={p}")

print ("\nFactor for (p-1) - should be r:",libnum.gcd(p-1,r))
print ("Factor for (p+1) - should be s:",libnum.gcd(p+1,s))
print ("Factor for (r-1) - should be t:",libnum.gcd(r-1,t))