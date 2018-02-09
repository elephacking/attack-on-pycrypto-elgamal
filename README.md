# Attack on the ElGamal implementation in PyCrypto

*UPDATE:* PyCrypto's implementation does not only allow chosen-plaintext attacks, but also ciphertext-only attacks. In some sense, this is what our source code already does anyways. More precisely, the attacker computes the Legendre symbol of the ciphertext and correlates with the Legendre symbols of the public key and Elgamal's random coin ($g^r$).


Here is the original README:

Chosen-plaintext attack on the ElGamal implementation in PyCrypto

All versions of PyCrypto generate weak key parameters. Specifically, Elgamal encryption takes places over Z*_p where the DDH does not hold. By computing the Legendre symbol, the attacker breaks IND-CPA.

Authors:
     Weikeng Chen and Erik-Oliver Blass

# Related post
https://github.com/dlitz/pycrypto/issues/253



# Test result on Travis
[![Build Status](https://www.travis-ci.org/TElgamal//attack-on-pycrypto-elgamal.svg?branch=master)](https://travis-ci.org/TElgamal/attack-on-pycrypto-elgamal)
Please check the following link for a third-party running trace: https://travis-ci.org/TElgamal/attack-on-pycrypto-elgamal
