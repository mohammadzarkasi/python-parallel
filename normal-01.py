import threading as th
import time

start = time.perf_counter()

def f1():
    print('memulai fungsi f1...')
    time.sleep(5)
    print('fungsi f1 selesai')

def f2():
    print('memulai fungsi f2...')
    time.sleep(3)
    print('fungsi f2 selesai')

f1()
f2()

finish = time.perf_counter()

print('program selesai', round(finish - start), 'detik')