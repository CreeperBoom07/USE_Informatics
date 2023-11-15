s = open('files/24_2505.txt').readline().strip()
d = {}
for i in range(1, len(s)-1):
    if s[i-1] == s[i+1]:
        d[s[i]] = d.get(s[i], 0) + 1
mx = max(sorted(d), key=lambda x: d[x])
print(mx, d[mx])
# W1608
