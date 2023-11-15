s = open('files/#1.txt').readline()

c = m = 0
for i in range(len(s)):
    if s[i] == 'B':
        c += 1
        m = max(m, c)
    else:
        c = 0
print(m)
