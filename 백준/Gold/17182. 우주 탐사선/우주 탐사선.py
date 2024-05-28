import sys
input = sys.stdin.readline

def backT(visit, val, now):
    global minValue
    if val > minValue:
        return

    if sum(visit) == N:
        if minValue > val:
            minValue = val
            return

    for i in range(N):
        if visit[i] == 0 and now != i:
            visit[i] = 1
            backT(visit, val + MAP[now][i], i)
            visit[i] = 0

    return

N, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        for k in range(N):
            if i == k or j == k:
                continue
            if MAP[i][k] > MAP[i][j] + MAP[j][k]:
                MAP[i][k] = MAP[i][j] + MAP[j][k]

minValue = 999999999
visited = list(0 for _ in range(N))
visited[K] = 1
backT(visited, 0, K)
print(minValue)