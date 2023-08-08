def f(line):
    d = {}
    for n in line:
        d[n] = d.get(n, 0) + 1
    s = []
    for key in d:
        if d[key] == 2:
            s.append(key)
    if len(s) == 3:
        s.sort()
        return s[0]**2 + s[1]**2 == s[2]**2


with open('./9_7030.csv') as file:
    lst = []
    for line in file:
        temp = [int(x) for x in line.split(';')]
        lst.append(temp)

k = 0
for line in lst:
    if f(line):
        k += 1
print(k)

# 148
