import threading as th
import time
import multiprocessing as mp



def f1():
    print('memulai fungsi f1...')
    time.sleep(5)
    print('fungsi f1 selesai')

def f2():
    print('memulai fungsi f2...')
    time.sleep(3)
    print('fungsi f2 selesai')


def jalankan():
    start = time.perf_counter()
    print('membuat process untuk fungsi f1 dan f2')
    p1 = mp.Process(target=f1)
    p2 = mp.Process(target=f2)


    print('menjalankan process...')
    p1.start()
    p2.start()


    print('memanggil fungsi join')
    p1.join()
    print('f1 telah di-join')
    p2.join()
    print('f2 telah di-join')


    # print('program selesai')
    finish = time.perf_counter()

    print('program selesai', round(finish - start,2), 'detik')

if __name__ == '__main__':
    jalankan()