with open('9 (1).csv') as file:
    data = [[int(n) for n in line.split(',')] for line in file]

k = 1
lst = []
for line in data:
    if len(line) == len(set(line)):
        a, b, c, d, e = sorted(line)
        if 2*a*b <= c + d + e:
            lst += [k]
    k += 1
print(sum(lst)/len(lst))           
# 3222
