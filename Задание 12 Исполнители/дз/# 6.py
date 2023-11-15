s = '>' + 11*'1' + 12*'2' + 30*'3'
while any(x in s for x in ('>1', '>2', '>3')):
    s = s.replace('>1', '22>', 1)
    s = s.replace('>2', '2>', 1)
    s = s.replace('>3', '1>', 1)
print(sum(int(x) for x in s if x != '>'))
# 98
