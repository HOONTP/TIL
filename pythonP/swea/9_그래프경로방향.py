T = int(input())

def findroot(n, G, arr):
    stack = []
    visted = [0]*100
    visted[n] = 1
    while True:
        if n == G:
            return 1
        for w in range(V+1):
            if arr[n][w] == 1 and visted[w] == 0:
                stack.append(n)
                n = w
                visted[n] = 1
                break
        else:
            if stack:
                n = stack.pop()
            else:
                return 0
    return


for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0]*100 for _ in range(V+1)]

    for i in range(E):
        a, b = map(int, input().split())
        arr[a][b] = 1

    S, G = map(int, input().split())

    print(f'#{tc}', findroot(S, G, arr))