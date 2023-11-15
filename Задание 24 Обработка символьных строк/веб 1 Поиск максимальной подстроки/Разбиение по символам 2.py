s = open('files/24var04.txt').readline().strip()
s = s.split('AB')
m = 0
for i in range(len(s)-21):
    c = 'AB'.join(s[i:i+22])
    m = max(m, len(c))
print(m)
# 10005
