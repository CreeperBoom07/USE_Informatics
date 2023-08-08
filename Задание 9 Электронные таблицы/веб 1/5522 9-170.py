from functools import reduce
k = 0
with open(file='9-170.csv', mode='r', encoding='utf-8') as file:
    for line in file:
        a = [int(i) for i in line.split(',')]
        a3 = [i for i in a if a.count(i) == 3]
        a1 = [i for i in a if a.count(i) == 1]
        if len(a3) == 3 and len(a1) == 3 and sum(a1)*3 <= reduce(lambda x, y: x*y, a3, 1):
            k += 1
print(k)

# 134
