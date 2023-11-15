s = open('files/24_2251.txt').readline().strip()
s = s.split('D')
m = 0
for i in range(len(s)-2):
    c = 'D'.join(s[i:i+3])
    m = max(m, len(c))
print(m)
# 373
