s = open('files/24-157.txt').readline().strip()
while 'OREOREO' in s:
    s = s.replace('OREOREO', 'OREO OREO')
# ИЛИ
k = 0
for i in range(len(s)-3):
    if s[i:i+4] == 'OREO':
        k += 1
print(k)
