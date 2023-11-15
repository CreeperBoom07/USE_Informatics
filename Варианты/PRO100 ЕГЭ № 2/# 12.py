s = '>' + 26*'1' + 10*'2' + 14*'3'

while any(x in s for x in ('>1', '>2', '>3')):
    s = s.replace('>1', '22>')
    s = s.replace('>2', '2>')
    s = s.replace('>3', '1>')
print(sum(int(x) for x in s if x != '>'))
# 138
