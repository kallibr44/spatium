from x11_hash import *
import hashlib

import pyscrypt
def scrypt(text):
 hashed = pyscrypt.hash(password = bytes(text, encoding='utf-8'),
                       salt = b'seasalt',
                       N = 1024,
                       r = 1,
                       p = 1,
                       dkLen = 32)
 return hashed[2:-1]

if __name__=='__main__':
 text = input("Введите текст для хэш: ")
 type = input("Введите тип хэш: \n 1.SHA-256 \n 2. Scrypt \n 3. X11 \n")
 if type == "1":
   print("Текст: %s \n Хэш SHA-256: %s" %(text, hashlib.sha256(bytes(text, encoding='utf-8')).hexdigest()))
 elif type == "2":
   print("Текст: %s \n Хэш Scrypt: %s" % (text,scrypt(text).hex()))
 elif type == "3":
   print("Текст: %s \n Хэш X11: %s" % (text,getPoWHash(bytes(text, encoding='utf-8'))[2:-1].hex()))
