T = int(input())

def backT(S, visted, sums):
    global mn
    if len(visted) == N-1:
        sums += arr[S][0]
        if sums < mn:
            mn = sums
    for w in range(1, N):
        if w not in visted:
            visted.append(w)
            backT(w, visted, sums+arr[S][w])
            visted.pop()


    pass

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mn = 999999999
    backT(0, [], 0)
    print(f'#{tc}', mn)