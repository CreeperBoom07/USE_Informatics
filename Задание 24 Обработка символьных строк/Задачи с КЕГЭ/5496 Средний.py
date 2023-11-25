s = open('files/24_5496.txt').readline().strip()

s = s.split('D')[1:-1]
m = 0
c = 'D'
for i in range(len(s)):
    if s[i].count('O') <= 2:
        c += s[i] + 'D'
        m = max(len(c), m)
    else:
        c = 'D'
print(m)
# 255
