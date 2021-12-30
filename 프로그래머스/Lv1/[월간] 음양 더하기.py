def solution(absolutes, signs):
    sum = 0
    for n, b in zip(absolutes, signs):
        sum += int(n if b else -n)
    return sum