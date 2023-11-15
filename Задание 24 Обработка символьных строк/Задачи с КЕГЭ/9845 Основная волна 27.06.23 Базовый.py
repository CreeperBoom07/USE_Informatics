s = open('files/24_9845.txt').readline().strip()
s = s.replace('C', 'A').replace('B', 'A')
s = s.replace('9', '8')
while 'AA' in s:
    s = s.replace('AA', 'A A')
while '88' in s:
    s = s.replace('88', '8 8')
s = s.split()
print(max(len(x) for x in s))
# 18
