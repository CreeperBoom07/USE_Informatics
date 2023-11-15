s = open('files/24-j3.txt').readline().strip()

print(s.count('K')-s.count('KOT'))
# или
s = s.replace('KOT', '*')
print(s.count('K'))
# 235061
