def solution(new_id):
    answer = ''

    # 1
    answer = new_id.lower()

    # 2
    char = '~!@#$%^&*()=+[{]}:?,<>/'
    answer = ''.join(i for i in answer if i not in char)

    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4
    if answer[0] == '.':
        answer = answer[1:]
    if len(answer) != 0 and answer[-1] == '.':
        answer = answer[:-1]

    # 5
    if answer == '':
        answer += 'a'

    # 6.
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

            # 7
    while len(answer) < 3:
        answer += answer[-1]

    return answer