import re
from itertools import permutations


def solution(expression):

    # 숫자와 사칙연산 분리
    ex=re.split('(\d+)', expression)[1:-1]

    # ex에 있는 연산자 파악(중복X)
    operators=[]
    for i in ex:
        if not i.isdigit() and i not in operators:
            operators.append(i)

    # 연산자 우선순위마다 값 계산
    results=[]
    for order in permutations(operators, len(operators)):
        ex_=ex.copy()
        for o in order:
            while o in ex_:
                oIdx=ex_.index(o)
                ex_[oIdx-1]=str(eval(''.join(ex_[oIdx-1:oIdx+2])))
                ex_.pop(oIdx+1)
                ex_.pop(oIdx)

        results.append(abs(int(ex_[0])))

    return max(results)