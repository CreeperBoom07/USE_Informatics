s = open('files/24_5551.txt').readline().strip()
c = m = 2
for i in range(1, len(s)-1):
    if s[i-1] == s[i+1] and s[i] != s[i-1]:
        c += 1
        m = max(c, m)
    else:
        c = 2
print(m)
# 1557
