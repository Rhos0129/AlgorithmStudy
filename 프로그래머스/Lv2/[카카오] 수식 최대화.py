from itertools import permutations

def solution(expression):
    operations = permutations(['-','+','*'], 3)
    answer = []
    for op in operations:
        a, b, c=op[0], op[1], op[2]
        result = []
        for aSplit in expression.split(a):
            bSplit = [f"({i})" for i in aSplit.split(b)]
            result.append(f'({b.join(bSplit)})')
        answer.append(abs(eval(a.join(result))))
    return max(answer)