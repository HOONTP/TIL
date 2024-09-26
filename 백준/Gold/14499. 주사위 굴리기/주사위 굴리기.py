import sys

input = sys.stdin.readline
from collections import deque

# 위 앞 아래 뒤 왼 오
dij = [0, (0, 1), (0, -1), (-1, 0), (1, 0)]


def rolling(dirction, x, y):
    global sq
    if dirction == 3:
        sq = [0, sq[2], sq[3], sq[4], sq[1], sq[5], sq[6]]
    elif dirction == 4:
        sq = [0, sq[4], sq[1], sq[2], sq[3], sq[5], sq[6]]
    elif dirction == 1:
        sq = [0, sq[5], sq[2], sq[6], sq[4], sq[3], sq[1]]
    elif dirction == 2:
        sq = [0, sq[6], sq[2], sq[5], sq[4], sq[1], sq[3]]

    if MAPS[x][y] == 0:
        MAPS[x][y] = sq[3]
    else:
        sq[3] = MAPS[x][y]
        MAPS[x][y] = 0
    print(sq[1])
    return


N, M, x, y, K = map(int, input().split())
MAPS = []
for n in range(N):
    MAPS.append(list(map(int, input().split())))


acts = list(map(int, input().split()))
sq = [0, 0, 0, 0, 0, 0, 0]

for act in acts:
    dx, dy = dij[act]
    nx, ny = x+dx, y+dy
    if 0 <= nx < N and 0 <= ny < M:
        x, y = nx, ny
        rolling(act, x, y)
