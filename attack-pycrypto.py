from Crypto.PublicKey import ElGamal
from Crypto import Random
import Crypto.Random.random

#Legendre for our specific setup with safe primes
def kronecker(x,p):
    q = (p-1)//2
    return pow(x,q,p)

def findQNR(p):
    r = Crypto.Random.random.randrange(2,p-1)
    while kronecker(r,p) == 1:
        r = Crypto.Random.random.randrange(2,p-1)
    return r

def findQR(p):
    r = Crypto.Random.random.randrange(2,p-1)
    return pow(r,2,p)

#Oracle; we use a 512 bit prime only for better performance
key = ElGamal.generate(512, Random.new().read)

wrong = 0
runs = 1000
print("Running experiment...")
for i in range(runs):
    #Adversary
    plaintexts = dict()
    plaintexts[0] = findQNR(key.p)
    plaintexts[1] = findQR(key.p)

    #Oracle
    challenge_bit = Crypto.Random.random.randrange(0,2)
    r =  Crypto.Random.random.randrange(1,key.p-1)
    challenge = key.encrypt(plaintexts[challenge_bit], r)

    #Adversary
    output = -1
    if (kronecker(key.y, key.p) == 1) or (kronecker(challenge[0], key.p) == 1):
        if kronecker(challenge[1], key.p) == 1:
            output = 1
        else:
            output = 0
    else:
        if kronecker(challenge[1], key.p) == 1:
            output = 0
        else:
            output = 1

    if output != challenge_bit:
        wrong = wrong + 1

print("Number of times adversary was wrong:" , wrong)
