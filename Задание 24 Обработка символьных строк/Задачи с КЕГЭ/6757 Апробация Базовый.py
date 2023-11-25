s = open('files/24_6757.txt').readline().strip()
s = s.replace('CFE', '*').replace('FCE', '*')
s = s.replace('C', ' ').replace('F', ' ').replace('E', ' ')
s = s.split()
print(max(len(x) for x in s))
# 103
