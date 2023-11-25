s = open('files/24_6798.txt').readline().strip()
sogl = 'CDF'
gl = 'AO'
m = 0
for x in 0, 1, 2, 3, 4, 5, 6, 7, 9, 10:
    c = 0
    for i in range(x, len(s)-2, 3):
        if s[i] in sogl and s[i+2] in gl:
            c += 1
            m = max(m, c)
        else:
            c = 0
print(m)
# 6
