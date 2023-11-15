s = open('files/24_7824.txt').readline().strip()

c = m = 2
for i in range(len(s)-2):
    if s[i] not in 'ABC' or s[i+1] not in 'ABC' or s[i+2] not in 'ABC':
        c += 1
        m = max(c, m)
    else:
        c= 2
print(m)
# 87
