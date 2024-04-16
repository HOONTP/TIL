from collections import deque
dxy = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if x != 0 or y != 0]

def searchMAP(i, j):
    global MAX_length
    q = deque()
    q.append((i, j, 1))
    visited = list(list(0 for _ in range(M)) for __ in range(N))
    visited[i][j] = 1
    while q:
        x, y, cnt = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0<=nx<N and 0<=ny<M:
                if MAPS[nx][ny] == 0 and visited[nx][ny] == 0:
                    q.append((nx, ny, cnt + 1))
                    visited[nx][ny] = 1
                if MAPS[nx][ny] == 1:
                    if MAX_length < cnt:
                        MAX_length = cnt
                    return
    return

N, M = map(int, input().split())

MAPS = list(list(map(int, input().split())) for _ in range(N))
MAX_length = 0
for i in range(N):
    for j in range(M):
        if MAPS[i][j] == 0:
            searchMAP(i, j)

print(MAX_length)