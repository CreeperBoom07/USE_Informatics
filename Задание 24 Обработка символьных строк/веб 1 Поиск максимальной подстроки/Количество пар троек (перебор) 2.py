s = open('files/24-215.txt').readline().strip()
s = s.replace('B', 'A').replace('C', 'A').replace('3', '1').replace('2', '1')
c = m = 0

for x in 0, 1, 2:
    c = 0
    for i in range(x,len(s)-2, 3):
        if s[i] + s[i+1] + s[i+2] == 'A11':
            c += 1
            m = max(c, m)
        else:
            c = 0
        

print(m)
# 165
