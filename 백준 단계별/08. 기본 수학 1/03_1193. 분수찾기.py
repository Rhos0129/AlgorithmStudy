n=int(input())

if n==1:
    print('1/1')
else:
    gcnt, ncnt=2, 1
    min=2
    while True:
        if min<=n<min+gcnt:
            nth=n-sum(range(gcnt))
            if gcnt%2==1:
                print(f'{gcnt - nth + 1}/{nth}')
            else:
                print(f'{nth}/{gcnt - nth + 1}')
            break
        min+=gcnt
        gcnt+=1