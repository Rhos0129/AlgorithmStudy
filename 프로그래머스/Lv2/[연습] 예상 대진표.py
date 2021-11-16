import math

def solution(n,a,b):

    round=1
    while True :
        if abs(a-b)==1 and min(a, b)%2==1 and max(a, b)%2==0:
            break

        a=math.ceil(a/2)
        b=math.ceil(b/2)
        round+=1

    return round