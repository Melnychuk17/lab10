# Сформувати функцію, що буде обчислювати факторіал заданого користувачем
# натурального числа n.

import timeit
# рекурсия
n=int(input('Enter the number: '))
def fact_rec(n):
    if n==1:
        return 1
    else:
        return n*fact_rec(n-1)
print(fact_rec(n))
# итерация
def fact_iter(n):
    count=1
    while n>1:
        count*=n
        n-=1
    print(count)
fact_iter(n)

t=timeit.timeit('"-".join(str(n)for n in range(100))', number=10000)
print(f'Program worked {t} seconds')

