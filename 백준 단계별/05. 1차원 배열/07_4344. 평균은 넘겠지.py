n=int(input())

for i in range(n):
    scores=[int(i) for i in input().split()]
    mean=sum(scores[1:])/scores[0]
    over=0
    for i in scores[1:]:
        if i>mean:
            over+=1
    print('{:.3f}%'.format(round(over/scores[0]*100, 3)))