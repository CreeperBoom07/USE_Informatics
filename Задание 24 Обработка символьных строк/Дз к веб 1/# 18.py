s = open('files/24_66.txt').readline().strip()
s = s.replace('KOT', '*')
s = s.replace('K', ' ').replace('O', ' ').replace('T', ' ')
s = s.split()
print(max(len(x) for x in s))
# 75
