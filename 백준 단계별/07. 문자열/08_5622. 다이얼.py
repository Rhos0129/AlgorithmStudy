grandMA=input()
char=['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ', '+-*/']

time=0
for s in grandMA:
    for c in char:
        if s in c:
            time+=char.index(c)+3
print(time)