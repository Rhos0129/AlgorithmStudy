num1, num2=input().split()

def lowhigh(num):
    lowNum=0; highNum=0
    for idx, i in enumerate(num):
        place = len(num) - idx - 1
        if i=='5' or i=='6':
            lowNum+=5*(10**place)
            highNum+=6*(10**place)
        else:
            lowNum+=int(i)*(10**place)
            highNum+=int(i)*(10**place)
    return lowNum, highNum

for i, j in zip(lowhigh(num1), lowhigh(num2)):
    print(i+j, end=' ')




