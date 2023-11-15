s = open('files/24-157.txt').readline().strip()
d = {x: s.count(x) for x in sorted(set(s))}
c = ''
m = 0
for x in d:
    if d[x] > m:
        c = x
        m = d[x]
print(c, m)
# W 38820
# или
c = max(d, key=lambda x: d[x])
print(c, d[c])
