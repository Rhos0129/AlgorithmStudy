def solution(participant, completion):
    answer = ''

    checkDic = {}
    for name in participant:
        if checkDic.get(name, 0) == 0:  # name이 없으면 0!!
            checkDic[name] = 1
        else:
            checkDic[name] += 1

    for name in completion:
        if checkDic.get(name) == 1:
            del checkDic[name]
        else:
            checkDic[name] -= 1

    return list(checkDic.keys())[0]