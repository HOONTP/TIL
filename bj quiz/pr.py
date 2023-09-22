import heapq

def dik(node, graph):
    q = []
    heapq.heappush(q, (0, node))

    lst = [float('inf')]*(V+1)
    lst[node] = 0
    lst[0] = 0
    visited = [0]*(V+1)

    while q:
        _, n = heapq.heappop(q)
        if visited[n] == 0:
            visited[n] = 1
        else:
            continue
        for i, w in graph[n]:
            if lst[n] + w < lst[i]:
                lst[i] = lst[n] + w
                heapq.heappush(q, (lst[i], i))
    return lst

for t in range(1, int(input())+1):
    V, E, X = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    reverse = [[] for _ in range(V+1)]
    for _ in range(E):
        e, s, w = map(int, input().split())
        arr[e].append((s, w))
        reverse[s].append((e, w))

    # visted =[0]*(V+1)
    value = dik(X, reverse)
    result = dik(X, arr)

    for i in range(1, V+1):
        value[i] += result[i]
    print(f'#{t}', max(value))