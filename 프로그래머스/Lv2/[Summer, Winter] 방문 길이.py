def solution(dirs):
    # 경로 기록하기
    history = []
    curLoc = [0, 0]
    for c in dirs:
        nextLoc = curLoc.copy()
        if c == 'U' and curLoc[1] < 5:
            nextLoc[1] += 1
        elif c == 'D' and curLoc[1] > -5:
            nextLoc[1] -= 1
        elif c == 'R' and curLoc[0] < 5:
            nextLoc[0] += 1
        elif c == 'L' and curLoc[0] > -5:
            nextLoc[0] -= 1

        if curLoc != nextLoc:
            history.append([curLoc, nextLoc])

        curLoc = nextLoc

    # 처음 걸어본 길 카운트
    cnt = 0
    for idx, item in enumerate(history):
        if item not in history[:idx] and item[::-1] not in history[:idx]:
            cnt += 1

    return cnt