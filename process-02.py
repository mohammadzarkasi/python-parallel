import time
import multiprocessing as mp

def f1(seq=0):
    print('memulai fungsi #' + str(seq))
    time.sleep(1)
    print('fungsi selesai #' + str(seq))


def jalankan():
    start = time.perf_counter()
    print('membuat process untuk fungsi dengan looping')
    
    n_process = 20
    processes = []
    for i in range(n_process):
        p = mp.Process(target=f1, args=[i])
        p.start()
        processes.append(p)
    
    for i in range(n_process):
        processes[i].join()
        # print('join process #' + str(i) + ' selesai')

    # print('program selesai')
    finish = time.perf_counter()

    print('program selesai', round(finish - start, 2), 'detik')

if __name__ == '__main__':
    jalankan()