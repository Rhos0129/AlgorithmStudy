# 제로베이스 데이터사이언스 과정 중 프로그래머스 스쿨의 코딩연습 문제

def solution(n, m):
    cnt=0
    for num in range(n, m+1):
        if str(num)==str(num)[::-1]:
            cnt+=1
    return cnt
