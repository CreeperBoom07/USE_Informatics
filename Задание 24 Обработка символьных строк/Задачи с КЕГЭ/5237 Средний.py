s = open('files/24_5237.txt').readline().strip()
s = s.split('Z')
print(max(len(x) for x in s if 'XX' not in x and 'YY' not in x))
# 15
