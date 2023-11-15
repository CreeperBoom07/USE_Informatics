s = open('files/24-157.txt').readline()
c = m = 3
for i in range(len(s)-3):
    if s[i] + s[i+1] + s[i+2] + s[i+3] != 'KEGE':
        c += 1
        m = max(m, c)
    else:
        c = 3
print(m)
# 873639
