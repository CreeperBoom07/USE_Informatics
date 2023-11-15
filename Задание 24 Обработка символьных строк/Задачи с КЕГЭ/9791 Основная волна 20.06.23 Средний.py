from string import ascii_uppercase as up
h = '0123456789' + up
h = h[:16]
s = open('files/24_9791.txt').readline().strip()
for i in up:
    if i not in h:
        s = s.replace(i, ' ')
s = s.split()
print(max(len(x) for x in s if x[0] != '0'))
# 21
