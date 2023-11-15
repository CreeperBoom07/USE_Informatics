s = open('files/24_7662.txt').readline().strip()
s = s.split('SOLO')
m = 0
for i in range(len(s)-4):
    c = 'SOLO'.join(s[i:i+5])
    a = set()
    for x in c:
        if x.isdigit():
            a.add(x)
    if len(a) > 5:
        m = max(len(c), m)
print(m)
# 425
