import numpy as np
import math
import matplotlib.pyplot as plt
import time
import datetime



def countingSort(array):
    size = len(array)
    output = [0] * size

    count = [0] * 10**6

    for i in range(0, size):
        count[array[i]] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]



time1 = [] 
time2 = [] 
elem1 = [] 
elem2 = [] 

for i in range(100):
    temp1 = []
    temp2 = []
    
    num_of_elem1 = np.random.randint(10, 1000)
    num_of_elem2 = np.random.randint(1000, 100000)
    
    elem1.append(num_of_elem1)
    elem2.append(num_of_elem2)
    
    for j in range(num_of_elem1):  
        temp1.append( round(np.random.randint(-100, 100),3) )
    
    start = datetime.datetime.now()
    countingSort(temp1) 
    end = datetime.datetime.now()
    time1.append(float((f'{(end-start).seconds}.{(end-start).microseconds}')))
    

    for j in range(num_of_elem2):  
        temp2.append( round(np.random.randint(-100, 100),3) )
    
    start = datetime.datetime.now()
    countingSort(temp2) 
    end = datetime.datetime.now()
    time2.append(float((f'{(end-start).seconds}.{(end-start).microseconds}')))
    
    temp1 = []
    temp2 = []


zipped_list1 = zip(elem1, time1)
zipped_list2 = zip(elem2, time2)
sorted_pairs1, sorted_pairs2 = sorted(zipped_list1), sorted(zipped_list2)
tuples1, tuples2 = zip(*sorted_pairs1), zip(*sorted_pairs2)
elem1, time1 = [list(tuple) for tuple in tuples1]
elem2, time2 = [list(tuple) for tuple in tuples2]


plt.plot(elem1, time1)
plt.xlabel('Liczba elementów tablicy')
plt.ylabel('Czas wykonania sortowania [s]')
plt.title(f'Analiza wyników (małe/średnie ilości)')
plt.show


plt.plot(elem2, time2)
plt.xlabel('Liczba elementów tablicy')
plt.ylabel('Czas wykonania sortowania [s]')
plt.title(f'Analiza wyników (duże ilości)')
plt.show
