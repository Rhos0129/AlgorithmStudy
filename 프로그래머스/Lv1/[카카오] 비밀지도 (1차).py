def solution(n, arr1, arr2):
    answer = []

    li1 = []
    for i in arr1:
        tmp = format(i, 'b')
        while len(tmp) < n:
            tmp = '0' + tmp
        li1.append(tmp)
    # print(li1)

    li2 = []
    for i in arr2:
        tmp = format(i, 'b')
        while len(tmp) < n:
            tmp = '0' + tmp
        li2.append(tmp)
    # print(li2)

    for i in range(n):
        tmp = ''
        for j in range(n):
            # print(li1[i], li2[i])
            if li1[i][j:j + 1] == '0' and li2[i][j:j + 1] == '0':
                tmp += ' '
            else:
                tmp += '#'
            # print(tmp)
        answer.append(tmp)

    return answer