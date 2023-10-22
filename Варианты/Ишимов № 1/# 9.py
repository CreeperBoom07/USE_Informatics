from itertools import permutations as pm

def f(lst):
    return any((a+b)%2!=0 and (c+d)%2!=0 for a, b, c, d in pm(lst))


with open('./9.csv') as file:
    data = [[int(x) for x in line.split(',')] for line in file]
s = 0
for line in data:
    tr = [x for x in line if line.count(x) == 3]
    dv = [x for x in line if line.count(x) == 2]
    if len(tr) == 3 and len(dv) == 4:
        if f(sorted(line)[:4]):
            s += sum(line)
print(s)
# 4675
