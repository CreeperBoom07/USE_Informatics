s = open('files/24_2250.txt').readline().strip()
s = s.split('A')
c = 0
m = 0
for i in range(len(s)-1):
    c = len('A'.join(s[i:i+2]))
    if c > m:
        m = c
print(m)
# 337
