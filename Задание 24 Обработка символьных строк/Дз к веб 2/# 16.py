s = open('files/24_2509.txt').readline().strip()
d = {x: s.count(x) for x in sorted(set(s))}
mx = max(d, key=lambda x: d[x])
mn = min(d, key=lambda x: d[x])
print(d[mx] - d[mn])
# 886
