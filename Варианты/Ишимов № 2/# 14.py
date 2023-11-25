from string import ascii_uppercase as up

abc = '0123456789' + up
abc = abc[:20]
for x in abc:
    for y in abc:
        n1 = int(f'5{y}4{x}{y}4HJ4', 20)
        n2 = int(f'4{y}6B{y}{x}1', 20)
        if (n1 + n2) % 15 != 0:
            break
    else:
        n1 = int(f'584{x}84HJ4', 20)
        n2 = int(f'486B8{x}1', 20)
        print(n1 + n2)
# 138834370725
