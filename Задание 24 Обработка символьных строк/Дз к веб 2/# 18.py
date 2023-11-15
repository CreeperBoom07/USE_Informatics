s = open('files/24_2504.txt').readline().strip()
d = {}
for i in range(len(s)-4):
    if s[i]+s[i+1]+s[i+3]+s[i+4] == 'CBBC':
        d[s[i+2]] = d.get(s[i+2], 0) + 1
mx = max(d, key=lambda x: d[x])
print(mx, d[mx])
# C5760
