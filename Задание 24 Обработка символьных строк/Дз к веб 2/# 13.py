s = open('files/24_1143.txt').readline().strip()
k = 0
for i in range(len(s)-10):
    if s[i] == 'A':
        for j in range(6, 10):
            if s[i + j] == 'F':
                k += 1
print(k)
