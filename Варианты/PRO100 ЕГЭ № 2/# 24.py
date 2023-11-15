with open('24_11465.txt') as file:
    s = file.readline()

for i in 'BC':
    s = s.replace(i, 'A')
    
s = s.replace('9', '8')
m = 0
k = 0
for x in range(len(s)-1):
    if s[x] + s[x+1] == 'AA' or s[x] + s[x+1] == '88':
        m = max(m, k+1)
        k = 0
    else:
        k += 1
print(m)        
# 18
