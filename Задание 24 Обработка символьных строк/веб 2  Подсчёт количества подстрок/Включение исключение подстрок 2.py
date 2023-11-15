s = open('files/24-j3.txt').readline().strip()
print(s.count('IKOT') + s.count('KOTI') - s.count('IKOTI'))

# или
s = s.replace('KOT', '*')
k = 0

for i in range(len(s)-1):
    if s[i] == '*':
        if s[i-1] == 'I' or s[i+1] == 'I':
            k += 1
print(k)
