s = 60*'4' + 60*'6' + 60*'8'

while any(i in s for i in ('46', '84', '86')):
    s = s.replace('46', '64')
    s = s.replace('84', '48')
    s = s.replace('86', '68')

print(s[24] + s[74] + s[149])
    
