def f(s):
    while '5555' in s or '888' in s:
        s = s.replace('5555', '88', 1)
        s = s.replace('888', '5', 1)

        
    return s


a = set()

for i in range(301, 1000):
    a.add(f(i*'5'))


print(len(a))
# 10
