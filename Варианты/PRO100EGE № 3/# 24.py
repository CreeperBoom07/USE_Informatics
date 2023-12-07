s = open('24_11892.txt').readline().strip()


m = 1000000
for i in range(len(s)):
    if s[i] == 'X':
        k = 1
        for j in range(i+1, len(s)):
            if s[j] == 'Y':
                break
            if s[j] == 'X':
                k += 1
            if k == 500:
                m = min(m, j-i+1)
                break
print(m)
