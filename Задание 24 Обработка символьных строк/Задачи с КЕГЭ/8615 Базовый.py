s = open('files/24_8615.txt').readline().strip()
m = c = 2
abc = 'ABCDEF'
for i in range(len(s)-2):
    if s[i] not in abc or s[i+1] not in abc or s[i+2] not in abc:
        c += 1
        m = max(c, m)
    else:
        c = 2
print(m)
# 846
