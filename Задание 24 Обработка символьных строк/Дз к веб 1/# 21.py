s = open('files/24_4627.txt').readline().strip()
s = s.replace('NPO', '*').replace('PNO', '*')
s = s.replace('N', ' ').replace('O', ' ').replace('P', ' ')
s = s.split()
print(max(len(x) for x in s))
# 327
