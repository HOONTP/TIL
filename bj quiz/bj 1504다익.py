import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**9)
import heapq

# 다른 방법은 3가지 리스트를 다 구해놓고
# 두개의 순서에 따라 더하는 값을 조정
def dijk(start, end):
    q = []
    distance = [float("inf")] * (V + 1)
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        w, v = heapq.heappop(q)
        if v == end:
            return w
        for weight, n in arr[v]:
            if distance[v]+weight < distance[n]:
                mid = distance[v] + weight
                distance[n] = mid
                heapq.heappush(q, (mid, n))

    return float("inf")

V, E = map(int, input().split())
arr = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    arr[u].append((w, v))
    arr[v].append((w, u))
m1, m2 = map(int, input().split())

sums = 0
sums += dijk(1, m1)
sums += dijk(m1, m2)
sums += dijk(m2, V)

sums2 = 0
sums2 += dijk(1, m2)
sums2 += dijk(m2, m1)
sums2 += dijk(m1, V)
if sums > sums2:
    sums = sums2
if sums == float("inf"):
    print(-1)
else:
    print(sums)