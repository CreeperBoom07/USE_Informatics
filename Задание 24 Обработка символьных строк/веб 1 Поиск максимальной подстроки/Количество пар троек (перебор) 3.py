s = open('files/24-204.txt').readline().strip()
c = m = 0
for x in 0, 1:
    c = 0
    for i in range(x, len(s)-1, 2):
        if s[i] + s[i+1] == 'AA' or s[i] + s[i+1] == 'CC':
            c += 1
            m = max(m, c)
        else:
            c = 0
print(m)
# 1310
