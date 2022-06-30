# Program : Decrypt files
# Description : Allow to decrypt file encrypted with the RSA key
# Date : 29/06/22
# Author : Christophe Lagaillarde
# Version : 1.0

import rsa


def decrypt(ciphertext: bytes, private_key: rsa.key.PrivateKey) -> bytes:
    try:
        return rsa.decrypt(ciphertext, private_key)

    except:
        return False

