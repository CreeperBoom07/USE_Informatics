s = open('files/24_9850.txt').readline().strip()
c = m = 0
for i in range(len(s)):
    if s[i] not in 'LISENOK':
        c += 1
        m = max(m, c)
    else:
        c = 0
print(m)
# 47
