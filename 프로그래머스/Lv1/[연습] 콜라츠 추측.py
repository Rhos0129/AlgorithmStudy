def solution(num):
    cnt = 0

    while True:

        # 결과확인
        if num == 1:
            break
        if cnt == 500:
            cnt = -1
            break

        # 계산
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        cnt += 1

    return cnt