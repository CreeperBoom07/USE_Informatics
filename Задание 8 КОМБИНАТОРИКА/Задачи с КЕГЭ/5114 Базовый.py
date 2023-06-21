from itertools import product as pd

k = 0
for x in pd('0123456', repeat=5):
    if x[0] != '0' and x.count('5') == 1:
        for i in range(5):
            if x[i] == '5' and i != 0 and i != 4:
                if int(x[i + 1]) % 2 != 0 and int(x[i - 1]) % 2 != 0:
                    k += 1
                    break
            elif x[i] == '5' and i == 0:
                if int(x[i + 1]) % 2 != 0:
                    k += 1
                    break
            elif x[i] == '5' and i == 4:
                if int(x[i - 1]) % 2 != 0:
                    k += 1
                    break
print(k)

# 1176
