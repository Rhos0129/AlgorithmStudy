n = int(input())
words = [input() for i in range(n)]

cnt = 0
for word in words:

    # 연속되는 문자만 제거
    wordList = list(word)
    wordList.append(0)

    noSerial = [wordList[idx] for idx in range(len(word))
                if wordList[idx] != wordList[idx + 1]]

    # 중복제거와 비교
    noSerial = sorted(noSerial)
    if noSerial == sorted(list(set(word))):
        cnt += 1

print(cnt)