# 제로베이스 데이터사이언스 과정 중 프로그래머스 스쿨의 코딩연습 문제

def solution(v):
    x, y=[], []
    for i, j in v:
        if i not in x:
            x.append(i)
        else:
            x.remove(i)

        if j not in y:
            y.append(j)
        else:
            y.remove(j)

    return [x[0], y[0]]