t=int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2=map(int, input().split())

    d=(abs(x1-x2)**2+abs(y1-y2)**2)**0.5 # 중심거리
    if d==0 and r1==r2:
        print(-1)
    elif abs(r1-r2)<d<r1+r2:
        print(2)
    elif d==r1+r2 or abs(r1-r2)==d:
        print(1)
    elif r1+r2<d or d<abs(r1-r2) or (d==0 and r1!=r2):
        print(0)