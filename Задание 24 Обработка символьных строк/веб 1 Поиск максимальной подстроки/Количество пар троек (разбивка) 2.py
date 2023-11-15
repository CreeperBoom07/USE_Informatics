s = open('files/24-215.txt').readline().strip()
s = s.replace('B', 'A').replace('C', 'A').replace('3', '1').replace('2', '1')
s = s.replace('A11', '*')
s = s.replace('A', ' ').replace('1', ' ')
print(max(len(x) for x in s.split()))
# 165
