from string import ascii_uppercase as up
m = 0
for x in up:
    s = open('files/24_7891.txt').readline().strip()
    s = s.split(x)
    m = max(m, max(len(x) for x in s )+2)
print(m)
    
# 9747
