n=int(input())

if n==1:
    print(1)
else:
    min=2
    group=2
    while True:
        if min<=n<min+6*(group-1):
            print(group)
            break
        min+=6*(group-1)
        group+=1