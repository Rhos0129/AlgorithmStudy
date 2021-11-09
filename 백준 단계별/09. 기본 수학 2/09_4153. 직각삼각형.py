while True:
    lst=list(map(int, input().split()))
    if lst==[0, 0, 0]:
        break

    lst.sort()
    print('right' if lst[0]**2+lst[1]**2==lst[2]**2 else 'wrong')

