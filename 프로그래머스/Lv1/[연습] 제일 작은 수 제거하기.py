def solution(arr):
    answer = arr
    answer.remove(min(arr))

    return answer if answer != [] else [-1]