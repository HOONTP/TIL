T = int(input())

def backT(S, visted, sums):
    global mn
    if len(visted) == N+1:
        sums += (abs(lst[1][0]-S[0])+abs(lst[1][1]-S[1]))
        if sums < mn:
            mn = sums
    mid = (999999999, (0,0))
    for w in lst:
        if w not in visted and w != lst[1]:
            if mid[0] > (abs(w[0]-S[0])+abs(w[1]-S[1])):
                mid = (abs(w[0]-S[0])+abs(w[1]-S[1]), w)
    visted.append(mid[1])
    backT(mid[1], visted, sums+mid[0])
    pass

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    mn = 999999999
    lst = []
    for i in range(0, 2*(N+2), 2):
        lst.append((arr[i], arr[i+1]))
    backT(lst[0], [lst[0]], 0)

    print(f'#{tc}', mn)