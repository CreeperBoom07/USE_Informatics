s = open('files/24_5810.txt').readline().strip()
s = s.replace('XYZ', '***').replace('XY', '**').replace('YZ', '**')
s = s.replace('X', ' ').replace('Y', ' ').replace('Z', ' ')
s = s.split()
print(len(max(s, key=len)))
# 44
 
