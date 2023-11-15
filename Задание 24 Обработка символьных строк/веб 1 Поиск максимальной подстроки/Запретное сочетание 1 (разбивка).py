s = open('files/24-157.txt').readline()
s = s.replace('ST', 'S T')
print(max(len(x) for x in s.split()))
# 6578
