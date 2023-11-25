s = open('files/24_5641.txt').readline().strip()
s = s.replace('NPO', 'NP PO')
s = s.replace('NP', 'N P').replace('PO', 'P O')
s = s.split()
print(max(len(x) for x in s))
# 123
