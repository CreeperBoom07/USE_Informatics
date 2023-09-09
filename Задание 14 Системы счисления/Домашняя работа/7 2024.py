from string import ascii_uppercase as Up
abc = '0123456789' + Up
abc = abc[:25]
n = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2024
s = ''
while n:
    s = abc[n%25] + s
    n //= 25
s = s.lstrip('0')
print(s.count('0'))
# 9
