""" Сформувати функцію для обчислення індексу максимального елемента масиву
n*n, де 1<=n<=5.
"""
import timeit
import random
import numpy as np

def max_iter():
    max,index=0,0
    for i in range(len(array)):
        if array[i]>max:
            max=array[i]
            index=i
    print(f'Maximal: {max} \nIndex: {index}')

def max_rec(array, i=0, j=0, i_max=0, j_max=0):
    if j== len(array[i]):
        i+=1
        j=0
    if i == len(array):
        return i_max, j_max
    if array[i][j]>array[i_max][j_max]:
        i_max = i
        j_max = j
    j += 1
    return max_rec(array, i_max, j_max, i, j)

n=int(input('Matrix size: '))
while n>5 or n<1:
    n=int(input('Matrix size: '))
array=np.array([[random.randint(1,20) for i in range(n)] for j in range(n)])
print(array)

t=timeit.timeit('"-".join(str(n)for n in range(100))', number=10000)
print(f'Program worked {t} seconds')