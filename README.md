# Attack on the ElGamal implementation in PyCrypto

Chosen plaintext attack on ElGamal Implementation of PyCrypto

All versions of PyCrypto generate weak key parameters. Specifically, Elgamal encryption takes places over Z*_p where the DDH does not hold. By computing the Legendre symbol, the attacker breaks IND-CPA.

Authors:
     Weikeng Chen and TElgamal (anonymous)

# Related post
https://github.com/dlitz/pycrypto/issues/253

