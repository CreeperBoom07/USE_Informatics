s = open('files/24_7356.txt').readline().strip()
s = s.replace('F', 'C').replace('D', 'C')
s = s.replace('O', 'A')
s = s.replace('CA', 'C A')
s = s.split()
for i in range(len(s)-5):
    c = s[i:i+5]
    m = max(len(c), m)
print(m)
### 16
