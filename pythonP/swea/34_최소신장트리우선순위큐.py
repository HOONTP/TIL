import heapq

def prim(start):
    sums = 0
    heapq.heappush(q, (0, start))
    while q:
        v, n = heapq.heappop(q)
        if visted[n]:
            continue
        visted[n] = 1
        sums += v
        for i in range(V+1):
            if lst[n][i] == 0 or visted[i]:
                continue
            heapq.heappush(q, (lst[n][i], i))
    return sums
for t in range(1, int(input())+1):
    V, E = map(int,input().split())
    lst = [[0]*(V+1) for _ in range(V+1)]
    q = []
    for _ in range(E):
        s, e, v = map(int, input().split())
        lst[s][e] = v
        lst[e][s] = v

    visted = [0] * (V+1)
    result = prim(0)
    print(f'#{t}', result)