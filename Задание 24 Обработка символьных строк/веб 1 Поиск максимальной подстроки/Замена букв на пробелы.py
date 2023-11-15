from string import ascii_uppercase as UP

s = open('files/24-s2.txt').readline()
for c in UP:
    if c not in 'ACDF':
        s = s.replace(c, ' ')
print(max(len(x) for x in s.split()))
# 7
