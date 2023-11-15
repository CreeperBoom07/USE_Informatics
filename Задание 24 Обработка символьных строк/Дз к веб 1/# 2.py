s = open('files/24_2420.txt').readline().strip()

c = m = 0
for i in range(len(s)):
    if s[i] in 'ABEF':
        c += 1
        if c > m:
            m = c
    else:
        c = 0
print(m)
# 20
