def solution(lottos, win_nums):
    cnt1 = 0;
    cnt2 = 0
    for i in lottos:
        if i in win_nums:
            cnt1 += 1
            cnt2 += 1
        if i == 0:
            cnt2 += 1

    if cnt1 == 0:
        cnt1 = 1
    if cnt2 == 0:
        cnt2 = 1

    return [7 - cnt2, 7 - cnt1]