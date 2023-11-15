m = ''
c = 0
for s in open('files/24_2508.txt'):
    c += s.count('C')
    if s.count('Q') >= m.count('Q'):
        m = s
        
d = {x: m.count(x) for x in sorted(set(m))}
print(d)
#C
print(c)
#C38412
