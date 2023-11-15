s = open('files/24-s2.txt').readline().strip()
d = {}
for i in range(len(s)-1):
    if s[i] == 'A':
        d[s[i+1]] = d.get(s[i+1], 0) + 1
print(d)
c = max(sorted(d), key=lambda x: d[x])
print(c, d[c])
# L 1567
