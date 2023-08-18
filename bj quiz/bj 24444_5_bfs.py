from collections import deque
import sys
input = sys.stdin.readline

def bfs(arr, R):
    visted = [0]*(N+1)
    q = deque()
    q.append(R)
    visted[R] = 1
    i = 2

    while q:
        n = q.popleft()
        for w in arr[n]:
            if visted[w] == 0:
                q.append(w)
                visted[w] = i
                i += 1
    return visted



N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
for i in arr:
    i.sort()#reverse=True하면 24445

result = bfs(arr, R)
for i in range(1, N+1):
    print(result[i])