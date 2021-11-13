from collections import deque

n=int(input()) # n행 n열

lst=[] # 게임판의 구역 (가중치가 표현된 인접행렬)
for i in range(n):
    lst.append(list(map(int, input().split())))

def bfs():
    queue=deque()
    visited = [[False] * (n+1) for i in range(n+1)]

    queue.append((1, 1))
    visited[1][1]=True

    while queue:
        x, y=queue.popleft()
        if lst[x-1][y-1]==-1:
            return "HaruHaru"

        nx=x+lst[x-1][y-1]
        ny=y+lst[x-1][y-1]

        if 1<=nx<=n and not visited[nx][y]:
            visited[nx][y] = True
            queue.append((nx, y))
        if 1<=ny<=n and not visited[x][ny]:
            visited[x][ny] = True
            queue.append((x, ny))

    return "Hing"

print(bfs())