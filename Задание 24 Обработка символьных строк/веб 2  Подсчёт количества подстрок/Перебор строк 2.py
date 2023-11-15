k = 0
for s in open('files/24-s1.txt'):
    for i in range(len(s)-3):
        if s[i] + s[i+2] + s[i+3] == 'ZRO':
            k += 1
            break
print(k)
# 59
