import sys
from encrypt import Encrypt
from decrypt import Descrypt
from gensafeprime import safe_prime_generator
from genprime import prime_generator
from makesafekey import makeSafeKey
from time import time

if (__name__ == "__main__"):
    '''
    python main_code_encrypt_decrypts.py todo parameters
    todo : 	-gen  sinh key -> parameters : so luong bit (max = 1024)
    		-enc  ma hoa
    		-dec  giai ma
    '''
    mode = sys.argv[1]

    if len(sys.argv) > 3 :
        print("To run: main_code_encrypt_decrypts.py too many input arguments.")
        print("WARNING: Must be provide enough arguments")
        exit

    if mode == "gen" and len(sys.argv) < 3:
        try:
            bits = sys.argv[2]
            prime_generator(int(bits))
            makeSafeKey()
        except IndexError:
            print("WARNING: Must be provide bit number of keys")
            exit
    elif mode == "enc":
        if len(sys.argv) > 2 :
            print("To run: main_code_encrypt_decrypts.py too many input arguments.")
            print("WARNING: Must be provide enough arguments")
            exit
        Encrypt()
    elif mode == "dec":
        if len(sys.argv) > 2 :
            print("To run: main_code_encrypt_decrypts.py too many input arguments.")
            print("WARNING: Must be provide enough arguments")
            exit
        Descrypt()
