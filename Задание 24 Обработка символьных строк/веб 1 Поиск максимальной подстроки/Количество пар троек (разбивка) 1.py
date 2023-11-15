s = open('files/24-196.txt').readline().strip()
s = s.replace('ZX', '*').replace('ZY', '*')
s = s.replace('X', ' ').replace('Y', ' ').replace('Z', ' ')
print(max(len(x) for x in s.split()))
# 177
