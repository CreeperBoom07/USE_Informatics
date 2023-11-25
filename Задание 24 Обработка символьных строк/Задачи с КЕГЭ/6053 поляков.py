s = open('files/24-241.txt').readline().strip()

m = 0
s = s.split('O')[1:-1]

c = 'O'
for i in range(len(s)):
    if s[i].count('F') <= 2:
        c += s[i] + 'O'
        m = max(m, len(c))
    else:
        c = 'O'

print(m)
