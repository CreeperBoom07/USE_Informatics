
lst = []  

with open('./17_6752.txt') as file:
    data = [int(num) for num in file]
    t = len([num for num in data if abs(num) % 3 == 0])
    for x in range(len(data)-1):
        if data[x] < 0 or data[x+1] < 0:
            if (data[x] + data[x+1]) < t:
                lst.append(data[x] + data[x+1])
                
print(len(lst), max(lst), sep='\n')
                
            
            
