

with open('./17_8007.txt') as file:
    data = [int(num) for num in file]
    s = 0
    for num in data:
        for digit in str(num):
            s += int(digit)
    lst = []
    for x in range(len(data)-1):
        if str(data[x]).endswith('10') ^ str(data[x+1]).endswith('10'):
            if (data[x] + data[x+1]) < s:
                lst.append(data[x] + data[x+1])
                
print(len(lst), min(lst), sep='\n')
