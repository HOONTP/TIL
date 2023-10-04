import sys
input = sys.stdin.readline
import heapq
# 이미 최단거리 -> 체크할 간선 -1 해주면 최단거리라면 값이 바뀔거고 아니라면 값이 바뀌지 않을거다.
def dijk(start):
    q = []
    heapq.heappush(q, (0, start))
    distance = [987654321]*(n+1)
    distance[start] = 0

    while q:
        w, node = heapq.heappop(q)
        for i in range(n+1):
            if arr[node][i] == -1:
                pass
            else:
                if arr[node][i] + w < distance[i]:
                    distance[i] = arr[node][i] + w
                    heapq.heappush(q, (distance[i], i))

    res = []
    for _ in lst:
        res.append(distance[_])
    return res

T = int(input())

for tc in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    arr = [[-1]*(n+1) for _ in range(n+1)]

    for _ in range(m):
        a, b, d = map(int, input().split())
        arr[a][b] = d
        arr[b][a] = d

    lst = []
    for tt in range(t):
        lst.append(int(input()))
    # s -> lst[:] 최단 경로 중 g-h 구간을 지나는 경우를 찾으면 된다.
    result = dijk(s)
    arr[g][h] -= 1
    arr[h][g] -= 1
    result2 = dijk(s)
    answer = []
    # print(lst)
    # print(result)
    # print(result2)
    for i in range(len(result)):
        if result[i] != result2[i]:
            answer.append(lst[i])
    print(*sorted(answer))