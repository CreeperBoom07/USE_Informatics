s = open('files/24-181.txt').readline().strip()
s = s.split('.')
m = 0
for i in range(len(s)-2):
    c = s[i] + '.' + s[i+1] + '.' + s[i+2]
    m = max(m, len(c))
print(m)
# 403 
