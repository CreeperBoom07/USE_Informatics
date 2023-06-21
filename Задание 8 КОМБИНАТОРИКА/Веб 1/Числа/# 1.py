'''  ЗАПОМНИ !!! Если работа с ЧИСЛАМИ, то ОБЯЗАТЕЛЬНА проверка: первый символ НЕ РАВЕН НУЛЮ!!!'''

from itertools import product as pd

k = 0
for x in pd('01234567', repeat=4):
    s = ''.join(x)
    if s[0] != '0' and int(s) % 4 == 0:
        k += 1
print(k)
