from string import ascii_uppercase as UP
s = open('files/24-1.txt').readline().strip()
for i in UP:
    s = s.replace(i, ' ')
s = s.split()
mn = 100000000000000000000000
for i in s:
    if i[0] != '0' and int(i)%2 == 0:
        mn = min(mn, int(i))
print(mn)
# 888
