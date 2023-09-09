from string import ascii_uppercase as Up

abc = '0123456789' + Up
abc = abc[:15]
n = 11*15**65 + 18*15**38 - 14*15**17 + 19*15**11 + 18338
s = ''
while n:
    s = abc[n%15] + s
    n //= 15
print(len(set(s)))
# 10

