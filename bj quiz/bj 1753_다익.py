import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**9)
import heapq
def dijk(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        w, v = heapq.heappop(q)
        for weight, n in arr[v]:
            if distance[v]+weight < distance[n]:
                mid = distance[v] + weight
                distance[n] = mid
                heapq.heappush(q, (mid, n))

V, E = map(int, input().split())

K = int(input())

distance = [float("inf")]*(V)

arr = [[] for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    arr[u-1].append((w, v-1))

dijk(K-1)

for i in distance:
    if i != float('inf'):
        print(i)
    else:
        print("INF")