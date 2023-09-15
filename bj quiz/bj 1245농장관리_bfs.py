import sys
input = sys.stdin.readline
from collections import deque

dij = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]
def bfs(n):
    q = deque()
    q.append(n)
    arr[n[0]][n[1]] = -1

    while q:
        i, j, num = q.popleft()

        for k in dij:
            ni = i+k[0]
            nj = j+k[1]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] >= 0:
                if arr[ni][nj] <= num:
                    q.append([ni, nj, arr[ni][nj]])
                    arr[ni][nj] = -1


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

while True:
    max = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] > max:
                max = arr[i][j]
                mij = [i, j, max]

    if max == 0:
        break

    bfs(mij)
    cnt += 1
print(cnt)

