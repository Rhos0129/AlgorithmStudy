def solution(numbers):
    answer = []

    for idx1, num1 in enumerate(numbers):
        for idx2, num2 in enumerate(numbers):
            if idx1 == idx2:
                continue
            else:
                answer.append(num1 + num2)

    answer = sorted(list(set(answer)))

    return answer