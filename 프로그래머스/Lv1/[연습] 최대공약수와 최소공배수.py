def solution(n, m):
    answer = []

    # 최대공약수
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0 and len(answer) == 0:
            answer.append(i)

    # 최소공배수
    answer.append(n * m // answer[0])

    return answer