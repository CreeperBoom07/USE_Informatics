s = open('files/24_4642.txt').readline().strip()
s = s.replace('B', 'A').replace('2', '1')
s = s.replace('A1', '*')
s = s.replace('A', ' ').replace('1', ' ')
print(max(len(x) for x in s.split()))
# 34
