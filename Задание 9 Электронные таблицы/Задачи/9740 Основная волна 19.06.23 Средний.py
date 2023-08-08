def f(line):
    d = {}
    for x in line:
        d[x] = d.get(x, 0) + 1

    val = list(d.values())

    if val.count(3) == 1 and val.count(1) == 4:
        s_n = 0
        s_p = 0
        for n in d:
            if d[n] == 1:
               s_n += n
            else:
                s_p = n
        return s_n / 4 <= s_p


with open('9_9740.csv') as file:
    lst = []
    for line in file:
        temp = [int(i) for i in line.split(',')]
        lst.append(temp)


k = 0
for line in lst:
    if f(line):
        k += 1
print(k)


# 36
