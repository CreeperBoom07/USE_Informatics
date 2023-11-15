s = open('files/24_10105 (1).txt').readline().strip()
s = s.split('T')
m = 0
for i in range(len(s)-100):
    c = 'T'.join(s[i:i+101])
    m = max(m, len(c))
print(m)
# 133
