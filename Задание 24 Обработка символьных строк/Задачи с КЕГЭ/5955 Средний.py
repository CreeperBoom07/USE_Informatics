s = open('files/24_5955.txt').readline().strip()
s = s.replace('F', 'C').replace('D', 'C').replace('O', 'A')
c = m = 3
for i in range(len(s)-3):
    if s[i:i+4] != 'CAAC':
        c += 1
        m = max(m, c)
    else:
        c = 3
print(m)
# 599
