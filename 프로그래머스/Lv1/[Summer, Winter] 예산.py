def solution(d, budget):

    newd = sorted(d)
    sum = 0
    count = 0
    for i in newd:
        sum += i
        count += 1
        if sum > budget:
            count = count - 1
            return count

    return min(len(newd), 100)