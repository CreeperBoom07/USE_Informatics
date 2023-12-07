s = open('files/24_11918.txt').readline().strip()
s = s.replace('E', 'A')
s = s.split('A')
m = 0
for i in range(len(s)-100):
    c = 'A'.join(s[i:i+101])
    m = max(m, len(c))
print(m)
