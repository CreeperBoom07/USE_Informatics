k = 0
for x in range(1, 51):

    if bin(x)[-3:] == '011':
    # if bin(x)[2:].endswith('011'):
        k += 1
print(k)
# Ответ 5
