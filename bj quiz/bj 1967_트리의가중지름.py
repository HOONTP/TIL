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

# import sys
# input = sys.stdin.readline
# from collections import deque
#
# def bfs(node):
#     q = deque()
#     q.append((node[1], node[0]))
#     mx = 0
#     while q:
#         wt, n = q.popleft()
#         if mx < wt:
#             mx = wt
#         for v, weight in lst[n]:
#             q.append((wt+weight, v))
#     return mx
#
# def possible(n):
#     if len(lst[n]) >= 2:
#         sums = []
#         result = 0
#         for i in lst[n]:
#             mid = bfs(i)
#             sums.append(mid)
#         sums.sort()
#         result = sums[-1] + sums[-2]
#         return result
#     elif len(lst[n]) == 1:
#         return bfs(lst[n][0])
#     else:
#         return -1
#
#
# N = int(input())
# lst = [[] for _ in range(N+1)]
#
# for _ in range(N-1):
#     a, b, w = map(int, input().split())
#     lst[a].append((b, w))
#
# mx_val = 0
# for i in range(1, N):
#     val = possible(i)
#     if val > mx_val:
#         mx_val = val
# print(mx_val)