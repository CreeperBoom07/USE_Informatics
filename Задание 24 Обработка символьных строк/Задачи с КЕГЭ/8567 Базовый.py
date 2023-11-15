s = open('files/24_8567.txt').readline().strip()
s = s.replace('B', 'A').replace('C', 'A').replace('D', 'A')
while 'AAA' in s:
    s = s.replace('AAA', 'AA AA')
s = s.split()
print(max(len(x) for x in s))
# 4362
