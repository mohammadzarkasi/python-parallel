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
    print('membuat process untuk fungsi dengan pool executor map')
    
    n_process = 5
    processes = []
    
    with ftr.ProcessPoolExecutor() as executor:
        args = [x+1 for x in range(n_process, -1, -1)]
        processes = executor.map(f1, args)
        
        for p in processes:
            print(p)
        

    # print('program selesai')
    finish = time.perf_counter()

    print('program selesai', round(finish - start, 2), 'detik')

if __name__ == '__main__':
    jalankan()