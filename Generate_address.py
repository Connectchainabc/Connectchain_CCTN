import binascii
import sha3 #pip install pysha3
from ecdsa import SigningKey, SECP256k1

priv = SigningKey.generate(curve=SECP256k1) #Private key
pub = priv.get_verifying_key() #Public key

keccak = sha3.keccak_256()
keccak.update( pub.to_string()) #keccak_256 Hash
address = "0x" + keccak.hexdigest()[24:]

priv_key = binascii.hexlify( priv.to_string())
pub_key = binascii.hexlify( pub.to_string())

print("Private key: " + priv_key.decode() )
print("Public key:  " + pub_key.decode() )
print("Address:     " + address)