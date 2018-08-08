from x11_hash import *
import hashlib
import pyscrypt
import psutil, os
import time
load = []
hash = []
def scrypt(text):
 hashed = pyscrypt.hash(password = bytes(text, encoding='utf-8'),
                       salt = b'seasalt',
                       N = 1024,
                       r = 1,
                       p = 1,
                       dkLen = 32)
 return hashed[2:-1]

def main(text):
 global load
 global sha256,scrypt,x11
 global hash
 sha256 = hashlib.sha256(bytes(text, encoding='utf-8')).hexdigest()
 scryp = scrypt(text).hex()
 x11 = getPoWHash(bytes(text, encoding='utf-8'))[2:-1].hex()
 pid = os.getpid()
 py = psutil.Process(pid)
 cpu = str(py.cpu_percent())
 ram = str(float('{:.3f}'.format(py.memory_info()[0]/2.**30)))
 print("CPU : " + cpu + "%")
 print("RAM : " + ram + " Gb")
 print("Текст: %s \n Хэш SHA-256: %s" %(text, sha256))
 print("Текст: %s \n Хэш Scrypt: %s" % (text,scryp))
 print("Текст: %s \n Хэш X11: %s" % (text,x11))
 hash = [sha256,scryp,x11]
 load = [cpu,ram]


if __name__=='__main__':
    start = time.time()
    text = input("Введите текст для хэш: ")
    main(text)
    d=time.time()-start
    file = open("log.txt","wt")
    file.write("Нагрузка CPU: {0} %\n Использовано RAM: {1} Gb\n Текст: {2} \n Хэш SHA-256: {3} \n хэш Scrypt: {4} \n хэш X11: {5}\n Время выполнения: {6} \n".format(load[0],load[1],text,hash[0],hash[1],hash[2],d))
    file.close()
    print("Complete with %s seconds \n" % (d))
