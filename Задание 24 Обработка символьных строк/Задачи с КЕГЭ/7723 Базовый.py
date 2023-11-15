s = open('files/24_7723.txt').readline().strip()
s = s.replace('8', '1').replace('R', 'D')
s = s.replace('11D', '*')
s = s.replace('D', ' ').replace('1', ' ')
s = s.split()
print(max(len(x) for x in s))
# 67
