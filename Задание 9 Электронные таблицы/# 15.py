with open('9_9832.csv') as file:
    data = [[int(n) for n in line.split(',')] for line in file]

for line in data:
    p = [n for n in line if line.count(n) == 2]
    np = [n for n in line if line.count(n) == 1]
    if len(p) == 4 and len(np) == 3:
        if line.count(max(line)) == 1:
            print(sum(line))
            break
        
  
            
