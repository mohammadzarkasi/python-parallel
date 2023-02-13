import threading as th
import time

def f1():
    print('memulai fungsi f1...')
    time.sleep(5)
    print('fungsi f1 selesai')

def f2():
    print('memulai fungsi f2...')
    time.sleep(3)
    print('fungsi f2 selesai')

print('membuat thread untuk fungsi f1 dan f2')
t1 = th.Thread(target=f1)
t2 = th.Thread(target=f2)

print('menjalankan thread...')
t1.start()
t2.start()

print('program selesai')