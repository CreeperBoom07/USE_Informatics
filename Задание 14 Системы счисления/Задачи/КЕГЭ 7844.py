from string import ascii_uppercase
s = '0123456789' + ascii_uppercase
s = s[:37]
print(s.index('V'))
for p in range(22, 37):
    for q in range(32, 37):
        for x in s[:p]:
            n1 = int(f'ALE{x}', p)
            n2 = int(f'DANOV', q)
            if (n1+n2) % 2023==0:
                print((n1+n2) / 2023)
                break


# 11097
