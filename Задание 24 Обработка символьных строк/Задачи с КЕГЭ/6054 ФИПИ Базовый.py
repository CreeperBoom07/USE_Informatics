s = open('files/24_6054.txt').readline().strip()
m = 0
for x in 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10:
    c = 0
    for i in range(x, len(s)-2, 3):
        if s[i] in 'BC' and s[i+1] in 'BC' and s[i+2] == 'A':
            c += 3
            m = max(m, c)
        else:
            c = 0
print(m)
# 6
