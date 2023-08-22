with open('./веб1/18-k3.csv') as file:
    data = [int(num) for num in file]
k = 0 
for num1 in range(len(data)-5):
    print()
    for num2 in range(num1+1, num1+6):
        print(data[num2], end=' ')
        if 1000 <= (data[num1] + data[num2]) <= 1500:
            k += 1
    
print(k)
