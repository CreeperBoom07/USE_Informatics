s = open('files/24-157.txt').readline().strip()
d = {x: s.count(x) for x in sorted(set(s), reverse=True)}

m = 10000000000000000000000
c = ''
for x in d:
    if d[x] < m:
        m = d[x]
        c = x
print(c, m)
