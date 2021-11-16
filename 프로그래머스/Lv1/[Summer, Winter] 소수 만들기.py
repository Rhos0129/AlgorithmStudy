from itertools import combinations

def solution(nums):
    answer = 0
    for item in list(combinations(nums, 3)):
        sumN = sum(item)
        for i in range(2, sumN):
            if sumN % i == 0:
                break
        else:
            answer += 1

    return answer