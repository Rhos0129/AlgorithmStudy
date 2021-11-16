def solution(s):
    result = []
    for i in s:
        if len(result) == 0 or i != result[-1]:
            result.append(i)
        else:
            result.pop()

    return 1 if result == [] else 0