import time
# from concurrent.futures import ProcessPoolExecutor
from concurrent import futures as ftr

def f1(duration=0):
    print('-->memulai fungsi #' + str(duration))
    time.sleep(duration)
    print('-->fungsi selesai #' + str(duration))
    return 'fungsi selesai #' + str(duration)


def jalankan():
    start = time.perf_counter()
    print('membuat process untuk fungsi dengan pool executor')
    
    n_process = 10
    processes = []
    
    with ftr.ProcessPoolExecutor() as executor:
        for i in range(n_process, 0, -1):
            p1 = executor.submit(f1, i)
            processes.append(p1)
        
        for p in processes:
            print(p.result())
        

    # print('program selesai')
    finish = time.perf_counter()

    print('program selesai', round(finish - start, 2), 'detik')

if __name__ == '__main__':
    jalankan()