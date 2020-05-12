""" Сформувати функцію для обчислення цифрового кореню натурального числа.
Цифровий корінь отримується наступним чином: необхідно скласти всі цифри заданого
 числа, потім скласти всі цифри знайденої суми і повторювати процес до тих пір, поки
 сума не буде дорівнювати однозначному числу, що і буде цифровим коренем заданого
 числа."""
import timeit
n=int(input('Enter yhe number: '))
def sum(n):
    if n<10:
        return n
    else:
        return n%10+sum(n//10)
def kor_rec(n):
    if n<10:
        return n
    else:
        return kor_rec(sum(n))
print(kor_rec(n))

def kor_iter(n):
    while n>=10:
        a=n%10
        b=n//10
        n=a+b
print(kor_iter(n))

t=timeit.timeit('"-".join(str(n)for n in range(100))', number=10000)
print(f'Program worked {t} seconds')





