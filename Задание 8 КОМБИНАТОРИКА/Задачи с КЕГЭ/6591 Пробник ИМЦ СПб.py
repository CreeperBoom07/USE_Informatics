from itertools import product as pd


def f(n: list):
    ch = 0
    nch = 0
    for i in n:
        if int(i) % 2 == 0:
            ch += int(i)
        else:
            nch += int(i)
    return ch < nch

k = 0
for x in pd('0123456', repeat=5):
    if x[0] != '0' and x.count('6') == 1 and f(x):
        k += 1
print(k)

# 1390
