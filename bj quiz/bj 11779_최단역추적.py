import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**9)
import heapq

def dijk(A, B):
    q = []
    heapq.heappush(q, (0, A))
    visited = [float('inf')] * (N+1)
    visited[A] = 0
    road[A] = A

    while q:
        w, n = heapq.heappop(q)
        # print(log)
        # visited[n] = 1
        if n == B:
            return w
        for weight, node in arr[n]:
            mid = w + weight
            if mid < visited[node]:
                visited[node] = mid
                road[node] = n
                heapq.heappush(q, (mid, node))

N = int(input())
M = int(input())

arr = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, W = map(int, input().split())
    arr[a].append((W, b))
A, B = map(int, input().split())
road = [0] * (N + 1)
result = dijk(A, B)

print(result)
ans = [B]
while B != A:
    ans.append(road[B])
    B = road[B]
print(len(ans))
print(*reversed(ans))

# 최소 비용
# 들르는 개수 - 무시
# 도시 번호 순서대로