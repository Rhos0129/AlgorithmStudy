from collections import deque

# 하나하나 탐색해야하고, 최단거리를 구해야하므로 bfs 사용
def solution(maps):

    n, m=len(maps),len(maps[0])

    moves=[[-1, 0], [1, 0], [0, 1], [0, -1]]

    def bfs():
        queue=deque()
        queue.append([1, 1, 1])

        while queue:
            x, y, cnt=queue.popleft()
            if x==n and y==m:
                break

            for move in moves:
                nx=x+move[0]
                ny=y+move[1]
                if 1<=nx<=n and 1<=ny<=m and maps[nx-1][ny-1]!=0:
                    queue.append((nx, ny, cnt+1))
                    maps[nx-1][ny-1]=0

        return cnt if maps[n-1][m-1] != 1 else -1 # 상대진영에 도착하지 못했을 경우 -1 반환

    return bfs()