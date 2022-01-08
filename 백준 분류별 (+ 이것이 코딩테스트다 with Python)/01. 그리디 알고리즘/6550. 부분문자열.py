while True:
    try:
        s, t=input().split()

        r=''
        for i in s:
            if i in t:
                for idx, j in enumerate(t):
                    if i==j:
                        r+=j
                        t=t[idx+1:] # 일치하는 문자 뒷부분에서 s의 다음문자를 검색하도록
                        break
            else:
                break

        print('Yes' if r==s else 'No')

    except:
        break