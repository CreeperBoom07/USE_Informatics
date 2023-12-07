s = open('24_11892.txt').readline().strip()

m = 10**10
#s = 'SFDSDXFEFSSFSEXEFWRWX'
s = s.split('X')
k = 0
for i in range(len(s)-499):
    c = 'X'
    for j in range(i, i+499):
        c += s[j] + 'X'

