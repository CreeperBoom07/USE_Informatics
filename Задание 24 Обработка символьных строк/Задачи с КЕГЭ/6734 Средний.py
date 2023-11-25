s = open('files/24_6734.txt').readline().strip()
s = s.split('.')
m = 10**10
for i in range(len(s)-6):
    c = '.'.join(s[i+1:i+7])
    m = min(len(c)+2, m)
print(m)
# 16
