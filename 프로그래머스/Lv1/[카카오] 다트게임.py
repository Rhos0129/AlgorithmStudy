def solution(dartResult):
    answer = []
    dartResult = dartResult.replace('10', 't')
    dartResult = list(dartResult)
    for i in range(len(dartResult)):
        if dartResult[i] == 't':
            dartResult[i] = '10'

    for i in range(1, len(dartResult)):
        if dartResult[i] == "S":
            answer.append(int(dartResult[i - 1]))
        elif dartResult[i] == "D":
            answer.append(int(dartResult[i - 1]) ** 2)
        elif dartResult[i] == "T":
            answer.append(int(dartResult[i - 1]) ** 3)

        if dartResult[i] == "*":
            if len(answer) >= 2:
                answer[-1] = answer[-1] * 2
                answer[-2] = answer[-2] * 2
            else:
                answer[-1] = answer[-1] * 2
        elif dartResult[i] == '#':
            answer[-1] = answer[-1] * (-1)

    return sum(answer)