s = open('files\#1.txt').readline()
s = s.replace('A', ' ').replace('C', ' ')
print(max(len(c) for c in s.split()))
