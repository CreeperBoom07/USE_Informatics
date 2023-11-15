s = open('files/24-157.txt').readline()

c = m = 1
for i in range(len(s)-1):
    if s[i] + s[i+1] != 'ST':
        c += 1
        m = max(m, c)
    else:
        c = 1
print(m)
# 6578
