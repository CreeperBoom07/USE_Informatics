k = 0
for s in open('files/24_2502.txt'):
    for i in range(len(s)-3):
        if s[i]+s[i+2]+s[i+3] == 'KGE':
            k += 1
            break
print(k)
# 48
