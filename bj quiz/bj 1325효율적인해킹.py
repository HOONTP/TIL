import sys
from collections import deque

input = sys.stdin.readline


def BFS(a):
    cnt = 1
    q = deque([a])
    visited = [0 for _ in range(N)]
    visited[a] = 1

    while q:
        x = q.popleft()
        for i in nList[x]:

            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
                cnt += 1
    return cnt

N, M = map(int, input().split())
nList = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    nList[b-1].append(a-1)

maxV = 0
result = []
for j in range(N):
    c = BFS(j)
    if maxV < c:
        maxV = c
        result = [j+1]
    elif maxV == c:
        result.append(j+1)

print(*result)