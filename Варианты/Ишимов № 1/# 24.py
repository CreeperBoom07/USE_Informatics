with open('24 (1).txt') as file:
    s = file.readline()

m = 0
k = 0
for x in s:
    if x not in 'ABCD':
        k += 1
    else:
        m = max(m, k)
        k = 0
print(m)
# 193
