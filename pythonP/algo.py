import sys
input = sys.stdin.readline
from collections import deque

def bfs(node):
    q = deque()
    q.append((0, node))
    mx = 0
    visited = [0] * (N+1)
    visited[node] = 1
    while q:
        wt, n = q.popleft()
        if mx < wt:
            mx = wt
            node = n
        for v, weight in lst[n]:
            if visited[v] == 0:
                q.append((wt+weight, v))
                visited[v] = 1
    return node, mx

N = int(input())
lst = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, w = map(int, input().split())
    lst[a].append((b, w))
    lst[b].append((a, w))


first, m = bfs(N)
second, mx_val = bfs(first)
print(mx_val)