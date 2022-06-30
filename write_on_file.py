# Program : Write on file
# Description : write on a given file
# Date : 30/06/22
# Author : Christophe Lagaillarde
# Version : 1.0

def write_on_file(file_name: str, data: bytes) -> None:
    file_to_write_on = open(file_name, 'wb')
    file_to_write_on.write(data)

    return None