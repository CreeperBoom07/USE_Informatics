s = open('files/24_1428.txt').readline().strip()
s = s.replace('XY', 'X Y').replace('XZ', 'X Z')
print(max(len(x) for x in s.split()))
# 25
