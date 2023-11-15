s = open('files/24_2498.txt').readline().strip()
k = 0
for i in range(len(s)-2):
    if s[i:i+3] == 'XIX':
        k += 1
print(k)
# 37255
