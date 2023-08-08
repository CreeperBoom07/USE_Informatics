def f(lst):
    d = {}
    for x in lst:
        d[x] = d.get(x, 0) + 1
    vals = list(d.values())
    return vals.count(2) == 2 and vals.count(1) == 3 


with open('9_9832.csv') as file:
    lst = []
    for line in file:
        temp = [int(n) for n in line.split(',')]
        lst.append(temp)

for line in lst:
    if f(line) and line.count(max(line)) == 1:
        print(sum(line))
        break

# 261
