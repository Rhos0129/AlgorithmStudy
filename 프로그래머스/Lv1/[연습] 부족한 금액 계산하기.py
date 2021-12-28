def solution(price, money, count):
    return max(sum(range(1, count+1))*price-money, 0)