s = open('files/24_8431.txt').readline().strip()
c = m = 0
for i in range(len(s)-2):
    if 'X' in s[i:i+3] and 'Y' in s[i:i+3] and 'Z' in s[i:i+3]:
        c = -2
    else:
        c += 1
        m = max(m, c)
print(m)
#15729 
