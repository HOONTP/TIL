import sys
input = sys.stdin.readline
from collections import deque

dij = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(i, j, num):
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        if numMAP[x][y] == 0:
            numMAP[x][y] = num
            countList[num] += 1
            sumList[num] += MAPS[x][y]
        else:
            continue
        for di, dj in dij:
            dx = x + di
            dy = y + dj
            if 0 <= dx < N and 0 <= dy < N and numMAP[dx][dy] == 0:
                diff = abs(MAPS[x][y] - MAPS[dx][dy])
                if L <= diff <= R:
                    q.append((dx, dy))

N, L, R = map(int, input().split())
MAPS = []
for _ in range(N):
    MAPS.append(list(map(int, input().split())))

result = 0 ## 이 부분 주의
num = 1
while num < N*N:
    numMAP = list(list(0 for _ in range(N)) for __ in range(N))
    num = 0
    countList = list(0 for _ in range(N**2+1))
    sumList = list(0 for _ in range(N**2+1))
    for i in range(N):
        for j in range(N):
            if numMAP[i][j] == 0:
                num += 1
                bfs(i, j, num)
    if max(countList) == 1:
        break
    result += 1 ## 이 부분 주의

    calList = list(0 for _ in range(N**2+1))
    for cal in range(N**2+1):
        if countList[cal] > 0:
            calList[cal] = sumList[cal]//countList[cal]
    for i in range(N):
        for j in range(N):
            k = numMAP[i][j]
            MAPS[i][j] = calList[k]
print(result)