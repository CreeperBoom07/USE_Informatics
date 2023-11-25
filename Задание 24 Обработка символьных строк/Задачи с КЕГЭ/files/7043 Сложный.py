
s = open('../files/24_7043.txt').readline().strip()
f = '0123456789ABCDEF'
m = len(s)
for i in range(len(s)):
    if s[i] == '0':
        k = 1
        for j in range(i+1, len(s)):
            if s[j] == f[k]:
                k += 1
                if k == 16:
                    m = min(j - i + 1, m)
                    break
print(m)
# 153