def dfs(n):
    stack = []
    stack.append(n)
    visted[n] = 1

    while stack:
        now = stack.pop()
        if graph[now]:
            for i in graph[now]:
                if visted[i] == 0:
                    visted[i] = 1
                    stack.append(i)
        pass
    return

for t in range(1, int(input())+1):
    N, M = map(int,input().split())
    lst = list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    visted = [0]*(N+1)
    for i in range(M):
        graph[lst[2*i]].append(lst[2*i+1])
        graph[lst[2*i+1]].append(lst[2*i])

    cnt = 0
    for i in range(1, N+1):
        if visted[i] == 0:
            cnt += 1
            dfs(i)
    print(f'#{t}', cnt)