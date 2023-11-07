import sys
input = sys.stdin.readline
from collections import deque
import pprint, heapq
di = (-1, 0, 1, 0)
dj = (0, -1, 0, 1)
# E가 적으면 크루스칼 E가 많으면 프림
# 크루스칼이 유리한 문제이지만 프림으로 풀어봤다.
def mapPing(a, b, num):
    q = deque()
    q.append((a, b))
    MAP[a][b] = num

    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<= ni <N and 0<= nj <M and MAP[ni][nj] == -1:
                q.append((ni, nj))
                MAP[ni][nj] = num

def numbering():
    global n
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 1:
                MAP[i][j] = -1

    for i in range(N):
        for j in range(M):
            if MAP[i][j] == -1:
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
    for n in range(1, max(N, M)):
        ni = i + di[k]*n
        nj = j + dj[k]*n
        if 0<= ni <N and 0<= nj <M:
            if MAP[ni][nj] == 0:
                continue
            else:
                if n-1 > 1:
                    connect_lst[number].add((n-1, MAP[ni][nj]))
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

        if count == n:
            return sums

        for weight, now in connect_lst[v]:
            if visited[now] == False:
                heapq.heappush(q, (weight, now))
    return False

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
n = 1

numbering() # n 제작

connect_lst = [set() for _ in range(n+1)]
getConnect() # 간선 찾기
# print(connect_lst)
# pprint.pprint(MAP)

result = prim(1)
if result == False:
    print(-1)
else:
    print(result)