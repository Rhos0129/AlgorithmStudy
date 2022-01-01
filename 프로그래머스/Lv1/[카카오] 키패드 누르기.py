def solution(numbers, hand):
    answer = ''

    # 9 => *, 10 => 0, 11 => # / n의 위치  => loc[n-1]
    loc = [(x, y) for x in (1, 2, 3, 4) for y in (1, 2, 3)]
    leftLoc = loc[9]  # *의 위치
    rightLoc = loc[11]  # #의 위치

    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            leftLoc = loc[n - 1]
        elif n in [3, 6, 9]:
            answer += 'R'
            rightLoc = loc[n - 1]
        else:

            numLoc = loc[n - 1] if n != 0 else loc[10]

            difL = abs(leftLoc[0] - numLoc[0]) + abs(leftLoc[1] - numLoc[1])
            difR = abs(rightLoc[0] - numLoc[0]) + abs(rightLoc[1] - numLoc[1])

            print(difL, difR)

            if difL < difR or (difL == difR and hand == 'left'):
                answer += 'L'
                leftLoc = numLoc
            else:
                answer += 'R'
                rightLoc = numLoc

    return answer