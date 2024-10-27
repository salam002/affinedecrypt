# before running this script, consider verifying the signature against file that was created
# openssl dgst -sha1 -verify key.pub -signature sig message

from Crypto.PublicKey import RSA
from Crypto.Hash import SHA

# import signature as integer
signature = int(open("sig", "rb").read().hex(),16)

# import public key file
pubkey = RSA.importKey(open("key.pub").read())

# modulus and exponent are then accessible as pubkey.n and pubkey.e, respectively
# reverse the signing operation and examine resulting value in hex
"%0128x%" % pow(signature, pubkey.e, pubkey.n)

# NOTE: %0128x% string specifies output should be 128 hex chars; not related to RSA
# output should be something like: ‘0001fffff...bf8c26eb5554b63c97b35bd6bf018948bc8d73ea’
# verify last 20 bytes of this output match the SHA-1 hash of the file, i.e.:
# SHA.new(b"CIS 5510 rul3z!").hexdigest()
