T = int(input())

def backT(S, visted, sums):
    global mn
    if sums > mn:
        return
    if len(visted) == N+1:
        sums += (abs(lst[1][0]-S[0])+abs(lst[1][1]-S[1]))
        if sums < mn:
            mn = sums
    for w in lst:
        if w not in visted and w != lst[1]:
            visted.append(w)
            backT(w, visted, sums+(abs(w[0]-S[0])+abs(w[1]-S[1])))
            visted.pop()
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