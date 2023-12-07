

def gen():
    for i in range(1, 10**10, 60):
        yield i
k = 0
lst = []
for x in range(0, 10**10, 4546):
    s = str(x)
    if s[0] == '8' and s[-2:] == '06' and '80' in s:
        k += 1

    if k == next(gen()):
        lst += [[x, x//4546]]
print(set(lst), sep='\n')



