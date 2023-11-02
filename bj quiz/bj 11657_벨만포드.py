import sys
input = sys.stdin.readline
import heapq

# 최대 N-1 만큼의 거리일 경우 때문에 N-1 회 돌리는거고
# 모든 간선을 한 번 최적화하는 행위가 포문에 담겨있음
def bellman_ford(start):
    distance = [float("inf")] * (V + 1)
    distance[start] = 0

    for _ in range(V - 1):
        for u, v, weight in edges:
            if distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight

    for u, v, weight in edges:
        if distance[u] + weight < distance[v]:
            print("-1")
            return

    # 결과 출력
    for i in range(2, V+1):
        if distance[i] < float("inf"):
            print(f"{distance[i]}")
        else:
            print(-1)

V, E = map(int, input().split())
edges = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

start_vertex = 1
bellman_ford(start_vertex)