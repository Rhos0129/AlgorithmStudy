def solution(left, right):
    answer = 0

    def check(n):
        result = []
        for i in range(1, n + 1):
            if n % i == 0:
                result.append(i)
        return len(result)

    for i in range(left, right + 1):
        if check(i) % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer