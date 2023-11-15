s = open('files/24-s2.txt').readline().strip()

d = {}
for i in range(len(s)-2):
    if s[i] == 'X' and s[i+2] == 'Z':
        d[s[i+1]] = d.get(s[i+1], 0) + 1

c = max(sorted(d, reverse=True), key=lambda x: d[x])
print(c, d[c])
#X73
