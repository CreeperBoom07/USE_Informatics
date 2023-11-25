s = open('files/24_5444.txt').readline().strip()
m = 0
for i in range(len(s)-2):
    if s[i] == s[i+1] == s[i+2]:
        c = 3
        for x in range(i+3, len(s)-2, 3):
            if s[x] == s[x+1] == s[x+2]:
                c += 3
                m = max(c, m)
            else:
                break
print(m)
# 15
