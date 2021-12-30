def solution(n, lost, reserve):

    answer = n-len(lost)
    lost.sort()
    reserve.sort()

    lostCopy=lost.copy()

    for i in lost:
        if i in reserve:
            reserve.remove(i)
            lostCopy.remove(i)
            answer+=1

    for i in lostCopy:
        if i-1 in reserve:
            reserve.remove(i-1)
            answer+=1
        elif i+1 in reserve:
            reserve.remove(i+1)
            answer+=1

    return answer