# Program : Store RSA keys in files
# Description : Store the RSA keys into files
# Date : 29/06/22
# Author : Christophe Lagaillarde
# Version : 1.0

import rsa


def store_rsa_keys_in_files(private_key: rsa.key.PrivateKey, public_key: rsa.key.PublicKey) -> None:

    with open('keys\\public_key.pem', 'wb') as file:
        file.write(public_key.save_pkcs1('PEM'))

    with open('keys\\private_key.pem', 'wb') as file:
        file.write(private_key.save_pkcs1('PEM'))

    return None

