import sys
input = sys.stdin.readline
import heapq
def dijk(start):
    distance = [float('inf')]*(V+1)
    q = []
    heapq.heappush(q, (0, start))

    while q:
        w, v = heapq.heappop(q)
        if w != 0 and v == start:
            return distance[start]
        if w > result:
            return distance[start]
        for weight, n in arr[v]:
            if w+weight < distance[n]:
                distance[n] = w+weight
                heapq.heappush(q, (distance[n], n))
    return distance[start]
V, E = map(int, input().split())

arr = [[] for _ in range(V+1)]

for __ in range(E):
    a, b, v = map(int, input().split())
    arr[a].append((v, b))

result = float('inf')
for i in range(1, V+1):
    ans = dijk(i)
    if ans < result:
        result = ans
if result == float('inf'):
    print(-1)
else:
    print(result)