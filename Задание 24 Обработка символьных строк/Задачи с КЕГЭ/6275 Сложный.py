s = open('files/24_6275.txt').readline().strip()
f = '0123456789ABCDEF'
a = set()
m = len(s)
for i in range(len(s)):
    if s[i] in f:
        a = {s[i]}
        for x in range(i+1, len(s)):
            if s[x] in f:
                a.add(s[x])
            if len(a) == 16:
                m = min(x-i+1, m)
                break
print(m)
# 42
