s = open('files/k7a-3.txt').readline()

c = m = 0
for i in range(len(s)):
    if s[i] in 'ACDF':
        c += 1
        m = max(m, c)
    else:
        c = 0
print(m)
# 23
