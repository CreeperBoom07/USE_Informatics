s = open('files/k8-12.txt').readline()

c = m = 1
char = ''
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        c += 1
        if c > m:
            m == c
            char = s[i]
    else:
        c = 1
print(char, m)
