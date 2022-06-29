# Program : Get RSA keys in files
# Description : Get the RSA keys from files
# Date : 29/06/22
# Author : Christophe Lagaillarde
# Version : 1.0

import rsa


def get_rsa_keys() -> tuple:
    public_key: rsa.key.PublicKey
    private_key: rsa.key.PrivateKey

    with open('keys\\public_key.pem', 'rb') as file:
        public_key = rsa.PublicKey.load_pkcs1(file.read())

    with open('keys\\private_key.pem', 'rb') as file:
        private_key = rsa.PrivateKey.load_pkcs1(file.read())

    return private_key, public_key