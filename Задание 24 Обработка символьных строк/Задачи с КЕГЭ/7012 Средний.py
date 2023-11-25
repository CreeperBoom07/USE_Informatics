k = 0
f = 'QWERTY'

for s in open('files/24_7012.txt'):
    c = 0
    for i in range(len(s)):
        if s[i] == f[c]:
            c += 1
        if c == 6:
            k += 1
            break
            
print(k)
# 4574
