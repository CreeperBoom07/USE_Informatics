s = open('files/24_865.txt').readline().strip()

c = m = 0
for i in range(len(s)):
    if s[i] not in 'CF':
        c += 1
        if c > m:
            m = c
    else:
        c = 0
print(m)
