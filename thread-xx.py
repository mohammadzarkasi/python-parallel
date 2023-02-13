import random
import threading

x = 200
y = 200

m1 = []
m2 = []
res = []

def myprint(arr, indent=''):
    # print(type(arr))
    if type(arr) != list:
        return
    if type(arr[0]) == list:
        print(indent, '[', sep='')
        for i in arr:
            myprint(i, indent=indent+' ')
        print(indent, ']', sep='')
    else:
        print(indent, arr)

for i in range(y):
    m11 = []
    m22 = []
    ress = []
    for j in range(x):
        m11.append(random.randint(-5,5))
        m22.append(random.randint(-5,5))
        ress.append('X')
    m1.append(m11)
    m2.append(m22)
    res.append(ress)


myprint(m1)
myprint(m2)
# print(res)

def mul(x1, y1, x2, y2):
    for y in range(y1, y2):
        m11 = m1[y]
        l11 = len(m11)
        # print('m11',m11)
        for x in range(x1, x2):
            res1 = 0
            for z in range(l11):
                r = m11[z] * m2[z][x]
                # print('m11z', m11[z], 'm2xz', m2[z][x], 'r', r)
                res1 += r
            # print('res1', res1)
            res[y][x] = res1

mul(0, 0, x, y)

# threads = []

# t1 = threading.Thread(target=mul, args=(0,0, x, y//2))
# threads.append(t1)
# t1.start()

# t2 = threading.Thread(target=mul, args=(0,y//2, x, y))
# threads.append(t2)
# t2.start()


# for index, thread in enumerate(threads):
#     thread.join()


print('res:')
myprint(res)