s = open('files/24_8510.txt').readline().strip()
s = s.replace('O', 'N').replace('P', 'N')
while 'NN' in s:
    s = s.replace('NN', 'N N')
s = s.split()
print(max(len(x) for x in s))
##m = c = 1
##for i in range(len(s)-1):
##    if s[i] not in 'NOP' or s[i+1] not in 'NOP':
##        c += 1
##        m = max(c, m)
##    else:
##        c = 1
##print(m)
# 57
