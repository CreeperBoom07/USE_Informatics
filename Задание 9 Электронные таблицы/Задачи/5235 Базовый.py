from itertools import permutations as pm

with open('./9_5235.csv') as file:
    data = [[int(num) for num in line.split(',')] for line in file]


k = 0
for line in data:
    if all((a+b)%2==0 for a, b in pm(line, r=2)):
        k += 1
print(k)
# 29
