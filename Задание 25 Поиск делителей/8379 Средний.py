
for x in range(0, 10**10, 137):
    s = str(x)
    if s.startswith('1234'):
        if len(s) > 4:
            if int(s[4:]) % (sum(int(i) for i in s[4:])**3) == 0:
                print(x)
#12340001
#123400010
#123437000
#1234000100
#1234370000
