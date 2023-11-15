s = open('files/24_279.txt').readline().strip()
s = s.replace('BOSS', '*')
k = 0
for i in range(len(s)-1):
    if s[i] == '*' and s[i-1] != 'J' and s[i+1] != 'J':
        k += 1
print(k)
# 2198
