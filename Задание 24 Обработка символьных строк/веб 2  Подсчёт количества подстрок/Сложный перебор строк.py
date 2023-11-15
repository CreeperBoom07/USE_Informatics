m = 'A'*1000
S = ''
for s in open('files/24-s1.txt'):
    if s.count('A') < m.count('A'):
        m = s
    S += s
d = {x: m.count(x) for x in sorted(set(m.strip()))}
c = max(sorted(d, reverse=True), key=lambda x: d[x])
print(c)
#V
print(S.count('V'))
#38429
