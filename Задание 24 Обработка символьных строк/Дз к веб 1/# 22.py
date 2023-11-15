s = open('files/24_4643.txt').readline().strip()

s = s.replace('B', 'A').replace('2', '1')
c = m = 0

for x in 0, 1, 2:
    c = 0
    for i in range(x, len(s)-2, 3):
        if s[i] + s[i+1] + s[i+2] == '11A':
            c += 1
            m = max(m, c)
        else:
            c = 0
print(m)
# 67
