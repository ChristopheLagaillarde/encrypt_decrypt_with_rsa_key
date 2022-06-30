# Program : Encrypt files
# Description : Allow to decrypt file encrypted with the RSA key
# Date : 29/06/22
# Author : Christophe Lagaillarde
# Version : 1.0

import rsa


def encrypt(data: bytes, public_key: rsa.key.PublicKey):

    return rsa.encrypt(data, public_key)

