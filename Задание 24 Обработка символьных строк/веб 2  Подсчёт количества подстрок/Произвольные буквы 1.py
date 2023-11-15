s = open('files/24-157.txt').readline().strip()

k = 0
for i in range(len(s)-3):
    if s[i] + s[i+2] + s[i+3] == 'AEX':
        k += 1
print(k)
# 62
