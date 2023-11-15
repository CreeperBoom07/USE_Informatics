s = open('files/24_2419.txt').readline().strip()
s = s.replace('A', ' ').replace('B', ' ')
print(max(len(x) for x in s.split()))
# 11
