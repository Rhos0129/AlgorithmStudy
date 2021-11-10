t = int(input())

for _ in range(t):
    x, y = map(int,input().split())
    distance = y - x

    count = 0  # 이동 횟수
    move = 1  # count별 이동 가능한 거리
    sum = 0  # 이동한 거리의 합
    while sum < distance :
        count += 1
        sum += move  # count 수에 해당하는 move를 더함
        if count % 2 == 0 :
            move += 1
    print(count)