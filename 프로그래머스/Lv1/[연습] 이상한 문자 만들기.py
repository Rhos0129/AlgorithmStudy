def solution(s):
    answer = ''

    words = [str(word) for word in s.split(sep=' ')]

    for idx1, word in enumerate(words):
        for idx2, char in enumerate(word):
            answer += char.upper() if idx2 % 2 == 0 else char.lower()
        if idx1 != len(words) - 1:
            answer += ' '

    return answer