s = open('files/24-157.txt').readline()

while 'PPP' in s:
    s = s.replace('PPP', 'PP PP')
print(max(len(x) for x in s.split()))
# 79989
