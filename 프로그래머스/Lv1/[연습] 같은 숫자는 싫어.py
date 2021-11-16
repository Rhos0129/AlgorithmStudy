def solution(arr):
    result = []
    for item in arr:
        if result == [] or item != result[-1]:
            result.append(item)

    return result