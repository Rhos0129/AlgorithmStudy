def solution(n):
    # n -> 3진법
    change = ''
    tmp = n
    while tmp != 0:
        change += str(tmp % 3)
        tmp = tmp // 3

    # 뒤집어서 3진법 -> 10진법
    answer = 0
    for idx, num in enumerate(reversed(change)):
        answer += int(num) * 3 ** idx

    return answer