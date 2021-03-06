from x11_hash import *
import psutil, os, time, pyscrypt, hashlib,subprocess
load = []
hash = []
def scrypt(text):
 hashed = pyscrypt.hash(password = bytes(text, encoding='utf-8'),
                       salt = b'seasalt',
                       N = 1024,
                       r = 1,
                       p = 1,
                       dkLen = 32)
 return hashed[2:-1] # обрезаем готовый Scrypt хэш для того, чтобы избаиться от 'b', " ' " перед конвертацией в hex

def main(text):
 global load
 global sha256,scrypt,x11
 global hash
 pid = os.getpid() # получаем идентификатор процесса программы
 py = psutil.Process(pid)# Создаем объект "Процесс"
 sha256 = hashlib.sha256(bytes(text, encoding='utf-8')).hexdigest()
 scryp = scrypt(text).hex()
 x11 = getPoWHash(bytes(text, encoding='utf-8'))[2:-1].hex()
 cpu = str(psutil.cpu_prcent(interval=2))# считывание нагрузки на CPU. interval= кол-во секунд, сколько он будет считывать нагрузку.
 ram = str(float('{:.3f}'.format(py.memory_info()[1]/(10**6))))# ситчываем RAM нагрузку в байта и конвертируем в Mb (bytes*(10**6))
 print("CPU : " + cpu + "%")
 print("RAM : " + ram + " Mb")
 print("Текст: %s \n Хэш SHA-256: %s" %(text, sha256))
 print("Текст: %s \n Хэш Scrypt: %s" % (text,scryp))
 print("Текст: %s \n Хэш X11: %s" % (text,x11))
 hash = [sha256,scryp,x11]
 load = [cpu,ram]


if __name__=='__main__':
    text = input("Введите текст для хэш: ")
    start = time.time() # старт таймера для отслеживания времени отработки программы
    main(text)
    d=time.time()-start # запись времени отработки
    cpu_config = subprocess.check_output('lscpu', shell=True).strip().decode().split("\n") # собираем информацию о процессоре
    file = open("log.txt","wt")
    file.write("Модель процессора:{7}\n Количество ядер: {8}\n Нагрузка CPU: {0} %\n Использовано RAM: {1} Mb\n Текст: {2} \n Хэш SHA-256: {3} \n хэш Scrypt: {4} \n хэш X11: {5}\n Время выполнения: {6} \n".format(load[0],load[1],text,hash[0],hash[1],hash[2],d,cpu_config[12][11:],cpu_config[3][7:]))
    file.close()
    print("Complete with %s seconds \n" % (d))
