def solution(sizes):
    maxX = max([sorted(item)[0] for item in sizes])
    maxY = max([sorted(item)[1] for item in sizes])

    return maxX * maxY