s = open('files/24_11636.txt').readline().strip()
k = ka = last = 0
for x in s:
    if x == 'A':
        k += ka - (last=='A')
        ka += 1
    last = x
print(k)
        
# 42587173055
