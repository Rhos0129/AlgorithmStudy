import re
from collections import Counter


def solution(s):
    # 정규식을 이용하여 숫자만 검색 후 리스트에 담기
    numList = list(map(int, re.findall('\d+', s)))

    # 값을 count하여 dict으로 반환 >> {1:3} 1이 3개 존재
    numsCounter = Counter(numList)

    # count를 기준으로 정렬
    result = sorted(numsCounter, key=lambda x: numsCounter.get(x), reverse=True)

    return result