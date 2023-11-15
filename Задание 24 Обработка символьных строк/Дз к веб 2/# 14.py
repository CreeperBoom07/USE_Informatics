s = open('files/24_836.txt').readline().strip()
k = 0
for i in range(len(s)-4):
    s1 = s[i:i+5]
    if s1 == s1[::-1]:
        k += 1
print(k)
# 1521
