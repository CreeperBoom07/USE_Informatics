s = open('files/24_2427.txt').readline().strip()

c = m = s[0]
for i in range(1, len(s)):
    if s[i-1] > s[i]:
        c += s[i]
        if len(c) > len(m):
            m = c
    else:
        c = s[i]
print(m)
