s = open('24 (3).txt').readline().strip()
s = s.replace('++', ' ')
s = s.split()
s = [i.strip('+') for i in s]
print('.')
print(max(len(x) for x in s if '+' in x and len(x) > 1))

# 162
