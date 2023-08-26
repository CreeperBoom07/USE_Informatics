with open('./18_2159.csv') as file:
    data = [int(num) for num in file]
k = 0
for i in range(len(data)-1):
    for j in range(len(data)):
        if (j - i) >= 9:
           if (data[i] + data[j]) % 2 != 0:
               k += 1
print(k)

