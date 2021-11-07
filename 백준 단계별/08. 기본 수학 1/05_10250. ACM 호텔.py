t = int(input())  # t개의 테스트 데이터

for i in range(t):
    h, w, n=map(int, input().split()) # 층, 방, n번째
    floor=n%h if n%h!=0 else h # 층 = 나머지 (나누어 떨어진다면 꼭대기층)
    room=n//h+1 if n%h!=0 else n//h # 방 = 몫 (올림)
    print(floor*100+room)
