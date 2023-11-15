s = open('files/24_223.txt').readline().strip()

k = 0
for i in range(len(s)-2):
    if s[i:i+3] == 'TIK' or s[i:i+3] == 'TOK':
        k += 1
print(k)
# 31348
