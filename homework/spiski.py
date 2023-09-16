import random
import datetime


befpyz = datetime.datetime.now()

x = int(input('введите колличество чисел в списке-'))

#список0
N = x
spis = []
for i in range(x):
    spis.append(random.randint(0,999999))


now1 = datetime.datetime.now()
possp = now1 - befpyz
print('список создан за', possp.seconds, 'секунд')


#пузырьки
for i in range(N-1):
    for j in range(N-i-1):
        if spis[j] > spis[j+1]:
            spis[j], spis[j+1] = spis[j+1], spis[j]

now2 = datetime.datetime.now()
pospyz = now2 - possp
print('пузырьком отсортирован за', pospyz.second, 'секунд')


befshh = datetime.datetime.now()


#список1
N = x
spis1 = []
for i in range(x):
    spis1.append(random.randint(0,999999))

#шейкер
def shaker(array): 
    length = len(array) 
    swapped = True
    start_index = 0
    end_index = length - 1
    
    while (swapped == True): 
        
        swapped = False
          
        # проход слева направо
        for i in range(start_index, end_index): 
            if (array[i] > array[i + 1]) : 
                # обмен элементов
                array[i], array[i + 1] = array[i + 1], array[i] 
                swapped = True
  
        # если не было обменов прерываем цикл
        if (not(swapped)): 
            break

        swapped = False

        end_index = end_index - 1
  
        #проход справа налево
        for i in range(end_index - 1, start_index - 1, -1): 
            if (array[i] > array[i + 1]): 
                # обмен элементов
                array[i], array[i + 1] = array[i + 1], array[i] 
                swapped = True
 
        start_index = start_index + 1

shaker(spis1)


now3 = datetime.datetime.now()
possh = now3 - befshh
print('шейкером отсортированно за', possh.seconds, 'секунд')

#список2
N = x
spis2 = []
for i in range(x):
    spis2.append(random.randint(0,999999))


befpir = datetime.datetime.now()


#пирамидка
def piram(array):
    build_max_heap(array)
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        max_heapify(array, index=0, size=i)
 
def parent(i):
    return (i - 1)//2
 
def left(i):
    return 2*i + 1
 
def right(i):
    return 2*i + 2
 
def build_max_heap(array):
    length = len(array)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(array, index=start, size=length)
        start = start - 1
 
def max_heapify(array, index, size):
    l = left(index)
    r = right(index)
    if (l < size and array[l] > array[index]):
        largest = l
    else:
        largest = index
    if (r < size and array[r] > array[largest]):
        largest = r
    if (largest != index):
        array[largest], array[index] = array[index], array[largest]
        max_heapify(array, largest, size)

piram(spis2)

now4 = datetime.datetime.now()
pospir = now4 - befpir
print('пирамидкой отсортированно за', pospir.seconds, 'секунд')