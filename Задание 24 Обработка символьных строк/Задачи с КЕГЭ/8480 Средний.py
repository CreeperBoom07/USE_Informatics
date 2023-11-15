s = open('files/24_8480.txt').readline().strip()
s = s.replace('B', 'A').replace('C', 'A')
while 'AA' in s:
    s = s.replace('AA', 'A A')
s = s.split()
print(max(len(x) for x in s))
# 717
