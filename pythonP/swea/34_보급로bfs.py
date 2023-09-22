from collections import deque
dij = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    lst[x][y] = 0
    while q:
        i, j = q.popleft()
        for k in dij:
            ni = i + k[0]
            nj = j + k[1]
            if 0<= ni <N and 0<= nj <N:
                value = lst[i][j] + int(arr[ni][nj])
                if value < lst[ni][nj]:
                    lst[ni][nj] = value
                    q.append((ni,nj))

    pass
for t in range(1, int(input())+1):
    N = int(input())
    INF = 1e9
    arr = [input() for _ in range(N)]
    lst = [[INF]*N for _ in range(N)]

    bfs(0,0)
    print(f'#{t}', lst[N-1][N-1])