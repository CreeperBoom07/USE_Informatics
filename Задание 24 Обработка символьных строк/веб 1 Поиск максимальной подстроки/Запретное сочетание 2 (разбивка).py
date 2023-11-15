s = open('files/24-157.txt').readline()
s = s.replace('KEGE', 'KEG EGE ')
print(max(len(x) for x in s.split()))
# 873639
