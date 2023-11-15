s = open('files/24_9169.txt').readline().strip()
s = s.replace('BAD', ' ').replace('FAT', ' ')
s = s.split(' ')
m = 10**10
for i in range(len(s)-3):
    c = 'FAT'.join(s[i+1:i+4])
    m = min(len(c), m)
print(m)
# 10
