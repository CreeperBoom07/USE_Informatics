from string import ascii_uppercase as up
s = open('files/24_8959.txt').readline().strip()
s = s.replace('EA', '**')
s = s.replace('NPC', '***')
for i in up:
    s = s.replace(i, ' ')
s = s.split()
print(max(len(x) for x in s))
# 135
