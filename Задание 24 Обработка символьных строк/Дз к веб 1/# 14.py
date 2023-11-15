s = open('files/24_1145.txt').readline().strip()
s = s.split('D')
print(min(len(x) for x in s if len(x) != 0 )+2)
# 139
