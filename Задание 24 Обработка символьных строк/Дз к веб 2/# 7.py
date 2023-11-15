s = open('files/24_2500.txt').readline().strip()

k = 0
for i in range(len(s)-3):
    if s[i] == 'G' and s[i+2] == 'M' and s[i+3] == 'E':
        k += 1
print(k)
# 50
