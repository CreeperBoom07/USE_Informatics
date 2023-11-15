s = open('files/24_4546.txt').readline().strip()
c = m = 0

for x in 0, 1, 2:
    c = 0
    for i in range(x, len(s)-2, 3):
        if (s[i] == 'A' and s[i+2] == 'A') or (s[i] == 'C' and s[i+2] == 'C'):
            c += 1
            m = max(m, c)
        else:
            c = 0
print(m)
# 21
