s = open('files/24_2426.txt').readline().strip()
s = s.replace('A', ' ').replace('B', ' ').replace('C', ' ')
print(max(len(x) for x in s.split()))
# 20
