def solution(n, t, m, p):
    # 10진수를 n진수로 변환
    def notation(n, t):
        lst=[]
        lst.extend([str(i) for i in range(10)])
        lst.extend([chr(i) for i in range(65, 71)])

        result=''
        while True:
            if t<n:
                result+=lst[t]
                break
            result+=lst[t%n]
            t//=n

        return result[::-1]

    # 출력값 구하기
    nums=[]
    i=0
    while len(nums)<t*m:
        nums.extend(list(notation(n, i)))
        nums=nums[:t*m]
        i+=1

    return ''.join([n for n in nums[p-1::m]])
