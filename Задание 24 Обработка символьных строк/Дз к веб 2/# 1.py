s = open('files/24_2497.txt').readline().strip()
k = 0
for i in range(len(s)-4):
    if s[i:i+5] == 'XVIII':
        k += 1
print(k)
# 4113
