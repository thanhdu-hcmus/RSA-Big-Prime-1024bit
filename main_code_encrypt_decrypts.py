import sys
from encrypt import Encrypt
from decrypt import Descrypt
from gensafeprime import safe_prime_generator
from genprime import prime_generator
from makesafekey import makeSafeKey
if (__name__ == "__main__"):

    mode = sys.argv[1]
    bits = sys.argv[2]
    if (mode == "encrypt"):
        safe_prime_generator(int(bits))
        makeSafeKey()
        Encrypt()
    elif ( mode == "decrypt" ):
        Descrypt()