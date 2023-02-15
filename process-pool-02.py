import time
# from concurrent.futures import ProcessPoolExecutor
from concurrent import futures as ftr

def f1(seq=0):
    print('memulai fungsi #' + str(seq))
    time.sleep(1)
    print('fungsi selesai #' + str(seq))
    return 'fungsi selesai #' + str(seq)


def jalankan():
    start = time.perf_counter()
    print('membuat process untuk fungsi dengan pool executor')
    
    n_process = 40
    processes = []
    
    with ftr.ProcessPoolExecutor() as executor:
        for i in range(n_process):
            p1 = executor.submit(f1, [i])
            processes.append(p1)
        
        for p in ftr.as_completed(processes):
            print(p.result())
        

    # print('program selesai')
    finish = time.perf_counter()

    print('program selesai', round(finish - start, 2), 'detik')

if __name__ == '__main__':
    jalankan()