import sys
input = sys.stdin.readline
from collections import deque
import heapq

def tree(graph):
    start = 1
    q = []
    heapq.heappush(q, (0, start))
    visited = [0]*(V+1)
    mst_sums = 0
    while q:
        w, now = heapq.heappop(q)
        if visited[now] == 0:
            visited[now] = 1
            mst_sums += w
            for node, weight in graph[now]:
                if visited[node] == 0:
                    heapq.heappush(q, (weight, node))
    return mst_sums

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

# print(graph)
result = tree(graph)
print(result)