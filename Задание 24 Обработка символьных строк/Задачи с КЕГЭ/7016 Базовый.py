s = open('files/24_7016.txt').readline().strip()

m = 0
for i in range(len(s)):
    if s[i] == 'A':
        for j in range(i+1,len(s)):
            if s[j] == 'D':
                m = max(j-i+1, m)
                break
            if s[j] == 'A':
                break
    if s[i] == 'D':
        for j in range(i+1,len(s)):
            if s[j] == 'A':
                m = max(j-i+1, m)
                break
            if s[j] == 'D':
                break
print(m)
# 273
