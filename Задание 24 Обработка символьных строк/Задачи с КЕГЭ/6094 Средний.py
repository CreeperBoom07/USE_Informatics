s = open('files/24_6094.txt').readline().strip()
s = s.replace('XYZY', 'XYZ YZY')
s = s.replace('Z', 'X')
s = s.replace('XY', '*')
s = s.replace('X', ' ').replace('Y', ' ').replace('Z', ' ')
s = s.split()
print(max(len(x) for x in s))
# 8
