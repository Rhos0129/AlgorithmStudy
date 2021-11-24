# 제로베이스 데이터사이언스 과정 중 프로그래머스 스쿨의 코딩연습 문제

import heapq

def solution(no, works):
    if no > sum(works):
        return 0

    works = [-i for i in works]
    heapq.heapify(works) # max heap

    for _ in range(no):
        heapq.heapreplace(works, works[0] + 1) # heap[0]은 항상 가장 작은 값

    return sum([i**2 for i in works])