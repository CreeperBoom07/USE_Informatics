s = open('files/24_6060.txt').readline().strip()
k = 0
for i in range(len(s)):
    c = s[i:i+9]
    if  len(c) == 9 and c == c[::-1]:
        k += 1
print(k)
# 202820
