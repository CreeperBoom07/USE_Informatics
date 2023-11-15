s = open('files/24_2501.txt').readline().strip()
k = 0
for i in range(len(s)-4):
    if s[i]+s[i+2]+s[i+4] == 'AAA':
        k += 1
print(k)
# 42
