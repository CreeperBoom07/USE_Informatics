s = open('files/24_2499.txt').readline().strip()
k = 0
for i in range(len(s)-3):
    if s[i:i+4] == 'XXXX':
        k += 1
print(k)
# 12263
