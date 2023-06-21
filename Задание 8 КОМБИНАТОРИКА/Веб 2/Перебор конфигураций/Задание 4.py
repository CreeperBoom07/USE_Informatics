'''Рассматриваются числа, восьмеричная запись которых содержит
   ровно 10 знаков. Определите количество таких чисел, в восьмеричной
   записи которых ровно пять цифр 7 и при этом никакая нечётная цифра не стоит
   рядом с цифрой 7'''

from itertools import product as pd

k = 0

for x in pd('70ЧН', repeat=10):
    if x[0] != '0' and x.count('7') == 5:
        s = ''.join(x)
        if 'Н7' not in s and '7Н' not in s and '77' not in s:
            k += 3**(s.count('Ч')+s.count('Н'))
print(k)

