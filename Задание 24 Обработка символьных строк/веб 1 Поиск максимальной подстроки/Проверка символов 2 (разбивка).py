s = open('files/k7a-3.txt').readline()
s = s.replace('B', ' ').replace('E', ' ')

print(max(len(x) for x in s.split()))
# 23
