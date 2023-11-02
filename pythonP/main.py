import sys
input = sys.stdin.readline
from collections import deque
import pprint, heapq
di = (-1, 0, 1, 0)
dj = (0, -1, 0, 1)

def mapPing(a, b, num):
    q = deque()
    q.append((a, b))
    MAP[a][b] = num

    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<= ni <N and 0<= nj <M and MAP[ni][nj] == 1:
                q.append((ni, nj))
                MAP[ni][nj] = num

def numbering():
    global n
    # for i in range(N):
    #     for j in range(M):
    #         if MAP[i][j] == 1:
    #             MAP[i][j] = -1

    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 1:
                mapPing(i, j, n)
                n += 1
    n -= 1

def getConnect():
    for i in range(N):
        for j in range(M):
            number = MAP[i][j]
            if number != 0:
                for k in range(4):
                    connect_find(i, j, k, number)
    return

def connect_find(i, j, k, number):
    for l in range(1, max(N, M)):
        ni = i + di[k]*l
        nj = j + dj[k]*l
        if 0<= ni <N and 0<= nj <M:
            if MAP[ni][nj] == 0:
                continue
            else:
                if l-1 > 1:
                    connect_lst[number].add((l-1, MAP[ni][nj]))
                return
        else:
            return
    return

def prim(node):
    sums = 0
    count = 0
    visited = [False] * (n+1)
    q = []
    heapq.heappush(q, (0, node))

    while q:
        w, v = heapq.heappop(q)
        if visited[v] == False:
            visited[v] = True
            # print(w, visited)

            sums += w
            count += 1
        else:
            continue

        if count == n-1:
            return sums

        for weight, now in connect_lst[v]:
            if visited[now] == False:
                heapq.heappush(q, (weight, now))
    return False

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
n = 2

numbering() # n 제작

connect_lst = [set() for _ in range(n+1)]
getConnect() # 간선 찾기
# print(connect_lst)
# pprint.pprint(MAP)
# print(n)
result = prim(2)
if result == False:
    print(-1)
else:
    print(result)