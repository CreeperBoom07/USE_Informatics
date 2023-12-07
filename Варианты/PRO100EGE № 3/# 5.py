
for n in range(100, 1000):
    s = str(n)
    a = int(s[0])*int(s[1])
    b = int(s[1])*int(s[2])
    R = str(min(a, b))+str(max(a, b))
    if R == '621':
        print(n)
# 732
