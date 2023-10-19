import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**9)
import heapq

def dijk(A, B):
    q = []
    heapq.heappush(q, (0, A))
    visited = [float('inf')] * (N+1)
    visited[A] = 0
    load[A] = A

    while q:
        w, n = heapq.heappop(q)
        # print(log)
        print(load)
        print(visited)
        if n == B:
            return w
        for weight, node in arr[n]:
            sums = w+weight
            if sums < visited[node]:
                visited[node] = sums
                load[node] = n
                heapq.heappush(q, (sums, node))

N = int(input())
M = int(input())

arr = [[] for _ in range(N+1)]
load = [0] * (N + 1)

for _ in range(M):
    a, b, W = map(int, input().split())
    arr[a].append((W, b))
A, B = map(int, input().split())

result = dijk(A, B)
print(load)
print(result[0])
print(len(result[1]))
print(*result[1])

# 최소 비용
# 들르는 개수 - 무시
# 도시 번호 순서대로