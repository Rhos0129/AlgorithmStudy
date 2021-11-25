def solution(x):
    sumNum = sum([int(i) for i in list(str(x))])
    return x % sumNum == 0