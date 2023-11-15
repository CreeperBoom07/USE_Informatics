from string import ascii_uppercase as up
s = open('files/24_7688.txt').readline().strip()
s = s.replace('TXA', '***').replace('XA', '**').replace('XY', '**')
for i in up:
    s = s.replace(i, ' ')
s = s.split()
print(max(len(x) for x in s))
# 112
