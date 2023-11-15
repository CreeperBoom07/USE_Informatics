k = 0
for s in open('files/24_587.txt'):
    b = s.count('B') + s.count('В')
    a = s.count('A') + s.count('А')
    if (b*100)/a >= 105:
        k += 1
print(k)
# 3
