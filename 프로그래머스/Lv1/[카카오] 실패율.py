def solution(N, stages):
    answer=[]

    failRate={}
    userCnt=len(stages)
    for i in range(1, N+1):
        if userCnt==0:
            failRate[i]=0
        else:
            failRate[i]=stages.count(i)/userCnt
        userCnt-=stages.count(i)

    answer=sorted(failRate, key=lambda x: failRate[x], reverse=True)

    return answer