s = open('files/24-196.txt').readline().strip()

c = m = 0
for i in range(0, len(s), 2):
    if s[i]+s[i+1] == 'ZX' or s[i]+s[i+1] == 'ZY':
        c += 1
        if c > m:
            m = c
    else:
        c = 0
print(m)
