n=int(input())

for i in range(n):
    result=input()
    scores=[0]
    for i in result:
        if i=='O':
            scores.append(scores[-1]+1)
        else:
            scores.append(0)
    print(sum(scores))