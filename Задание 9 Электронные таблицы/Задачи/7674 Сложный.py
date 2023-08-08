def f(line):
    d = {}
    for n in line:
        d[n] = d.get(n, 0) + 1

    val = list(d.values())
    if val.count(1) == 3:
        s_n = []
        s_p = []
        for key in d:
            if d[key] == 1:
                s_n += [key]
            else:
                s_p += [key]
        return sum(s_n)/len(s_n) < sum(s_p)/len(s_p)


with open('9_7674.csv') as file:
    lst = []
    for line in file:
        temp = [int(x) for x in line.split(',')]
        lst.append(temp)


k = 0
for line in lst:
    if f(line):
        k += 1
print(k)

# 344
