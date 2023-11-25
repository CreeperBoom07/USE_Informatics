s = open('files/24_6636.txt').readline().strip()
for i in range(1, 6):
    if i % 2 == 0:
        s = s.replace(f'{i}', '0')
    else:
        s = s.replace(f'{i}', '1')
s = s.replace('01', '*')
s = s.replace('1', ' ').replace('0', ' ')
s = s.split()
print(max(len(x) for x in s))
# 10
