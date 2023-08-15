N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]

def dfs(arr, S):
    visted = []
    stack = [S]

    while stack:
        n = stack.pop()
        if n not in visted:
            visted.append(n)
            for i in sorted(arr[n], reverse=True):
                if i not in visted:
                    stack.append(i)
    return visted
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

result = dfs(arr, 1)
print(len(result)-1)