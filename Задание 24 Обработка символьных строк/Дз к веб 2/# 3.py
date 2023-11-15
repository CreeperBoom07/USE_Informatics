s = open('files/24_314.txt').readline().strip()
s = s.replace('OCK', '*')
print(s.count('*')-s.count('ST*'))
# 7626
