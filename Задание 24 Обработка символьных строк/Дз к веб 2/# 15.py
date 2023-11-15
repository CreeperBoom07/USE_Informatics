s = open('files/24_2506.txt').readline().strip()
d = {x: s.count(x) for x in sorted(set(s))}
c = max(d, key=lambda x: d[x])
print(c, d[c])
#W38820
