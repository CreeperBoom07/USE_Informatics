from string import ascii_uppercase as up
s = open('files/24_9552.txt').readline().strip()
s = s.replace('PCSGO', 'PC CSGO')
s = s.replace('PC', '**').replace('CSGO', '****')
for i in up:
    s = s.replace(i, ' ')

s = s.split()
print(max(len(x) for x in s))
# 90
