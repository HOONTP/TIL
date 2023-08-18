from collections import deque
import sys
input = sys.stdin.readline

def dfs(arr, R):
    visted_dfs = []
    stack = []
    stack.append(R)
    visted_dfs.append(R)
    while stack:
        # print(stack)
        # print(visted_dfs, 'vis')
        n = stack[-1]#이렇게 사용하자
        print(n)
        for w in arr[n]:
            if w not in visted_dfs:
                stack.append(w)
                visted_dfs.append(w)
                break
        else:
            if stack:
                stack.pop()#pop한 값을 n으로받으면 제자리 탐색이 1회 늘어남.
            else:
                return visted_dfs
    return visted_dfs


def bfs(arr, R):
    visted = []
    visted.append(R)
    q = deque()
    q.append(R)
    while q:
        n = q.popleft()
        for w in arr[n]:
            if w not in visted:
                q.append(w)
                visted.append(w)
    return visted

N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
for i in arr:
    i.sort()

result1 = dfs(arr, R)
result2 = bfs(arr, R)
print(*result1)
print(*result2)