def solution(array, commands):
    answer = []

    for item in commands:
        tmp = array[item[0] - 1:item[1]]
        tmp.sort()
        answer.append(tmp[item[2] - 1])

    return answer