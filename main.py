import rsa
from generate_rsa_keys import generate_rsa_keys
from store_rsa_keys_in_files import store_rsa_keys_in_files
from get_rsa_keys import get_rsa_keys
from encrypt import  encrypt
from decrypt import decrypt


def main() -> None:
    file_to_read = open('file_to_read.txt', 'r')
    normal_message = file_to_read.read()

    encrypted_message: bytes
    decrypted_message: str
    private_key: rsa.key.PrivateKey
    public_key: rsa.key.PublicKey

    (public_key, private_key) = generate_rsa_keys()

    store_rsa_keys_in_files(private_key, public_key)

    (private_key, public_key) = get_rsa_keys()
    encrypted_message = encrypt(normal_message, public_key)
    decrypted_message = decrypt(encrypted_message, private_key)

    print(normal_message)
    print(encrypted_message)
    print(decrypted_message)

    return None


if __name__ == '__main__':
    main()