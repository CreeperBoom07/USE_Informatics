s = open('files/24_8166.txt').readline().strip()
m = 0
for x in 0, 1, 2, 3:
    c = 0
    for i in range(x, len(s)-1, 2):
        if s[i] in 'ABC' and s[i+1] in 'ABC':
            c += 1
            m = max(m, c)
        else:
            c = 0
print(m)
# 9
