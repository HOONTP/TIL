T = int(input())

def bfs(arr, S):
    visted = [0] * (V+1)
    que = []
    que.append([S, 0])
    visted[S] = 1
    while que:
        n = que.pop(0)
        for w in arr[n[0]]:
            if w == G:
                return n[1]+1
            elif visted[w] != 1:
                que.append([w, n[1]+1])
                visted[w] = 1
    return 0

for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[] for _ in range(51)]

    for i in range(E):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    S, G = map(int, input().split())

    result = bfs(arr, S)

    print(f'#{tc}', result)