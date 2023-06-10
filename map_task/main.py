import matplotlib.pyplot as plt
import time
import sys

test = dict()
times_py=[]
sizes_py=[]
quantity=[]
for i in range(0, 5+1):
    c=10**i
    quantity.append(c)
    start = time.time()
    for j in range(1, c+1):
        test[j] = j
    end = time.time()
    times_py.append((end-start)*10**3)
    sizes_py.append(sys.getsizeof(test))

data = input().split()
times_cpp = list(map(int, data[::2]))
sizes_cpp = list(map(int, data[1::2]))

def paint_graph(name, x, y, xl, yl):
    plt.figure(name)
    plt.title(name)
    plt.plot(x, y)
    plt.xlabel(xl)
    plt.ylabel(yl)

paint_graph("DICT зависимость времени в мс от количества элементов", quantity, times_py, "elements", "ms")
paint_graph("DICT зависимость объёма памяти в байтах от количества элементов", quantity, sizes_py, "elements", "bytes")

quantity=[]
for i in range(0, 7+1):
    c=10**i
    quantity.append(c)

paint_graph("MAP зависимость времени в мс от количества элементов", quantity, times_cpp, "elements", "ms")
paint_graph("MAP зависимость объёма памяти в байтах от количества элементов", quantity, sizes_cpp, "elements", "bytes")

plt.show()