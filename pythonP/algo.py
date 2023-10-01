import sys
input = sys.stdin.readline
import heapq

def dijk(start, end):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        w, v = heapq.heappop(q)
        if v == end:
            return w
        if v * 2 <= E+1 and visited[v*2] == 0:
            heapq.heappush(q, (w, v * 2))
            visited[v*2] = 1
        if v + 1 <= E+1 and visited[v+1] == 0:
            heapq.heappush(q, (w+1, v+1))
            visited[v+1] = 1
        if v - 1 >= 0 and visited[v-1] == 0:
            heapq.heappush(q, (w+1, v-1))
            visited[v-1] = 1

    return float("inf")

V, E = map(int, input().split())
visited = [0]*(100002)

result = dijk(V, E)

print(result)