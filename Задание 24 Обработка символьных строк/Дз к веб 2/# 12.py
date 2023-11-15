k = 0
for s in open('files/24_2503.txt'):
    a = 0
    b = 0
    for i in range(len(s)-2):
        if s[i:i+3] == 'AOA':
            a += 1
        if s[i:i+3] == 'OAO':
            b += 1
    if a > b:
        k += 1
print(k)
# 55
n
