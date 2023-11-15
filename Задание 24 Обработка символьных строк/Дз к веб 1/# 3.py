s = open('files/24_2421.txt').readline().strip()
s = s.split('D')
print(max(len(x) for x in s))
# 44
