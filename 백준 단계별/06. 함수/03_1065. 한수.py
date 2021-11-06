def solve(n):
    cnt=0

    i=1
    while i<=n:

        flag=True
        preNum=0; d=0
        for idx, k in enumerate(str(i)):
            if idx==0:
                pass
            elif idx==1:
                d=preNum-int(k)
            else:
                if preNum-int(k)!=d:
                    flag=False
                    break
            preNum=int(k)

        if flag:
            cnt+=1

        i+=1

    return cnt

n=int(input())
print(solve(n))