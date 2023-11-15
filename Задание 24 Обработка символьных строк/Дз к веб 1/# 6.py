s = open('files/24_1040.txt').readline().strip()
c = m = 0
for i in range(len(s)):
    if s[i].isdigit():
        c += 1
        if c > m:
            m = c
    else:
        c = 0
print(m)
# 12
