s = open('files/24_4602.txt').readline().strip()
for i in 'CD':
    s = s.replace(i, 'B')
s = s.replace('A', 'O')
s = s.replace('BO', '*')
s = s.replace('B', ' ').replace('O', ' ')
print(max(len(x) for x in s.split()))
# 18
