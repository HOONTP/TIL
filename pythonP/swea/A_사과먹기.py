T = int(input())
'''
오앞 1 오뒤 2 왼 3 을 쓸 건지 백트래킹으로 구현할건지
'''
def iseeu(n, cnt, see):
    if n == final:
        print(f'#{tc}', cnt)
        return
    i, j = target[n][0], target[n][1]
    a, b = target[n+1][0], target[n+1][1]
    if see == 1: # 오 1 아 2 왼 3 위 4
        if i > a:# 우로 볼 때 대상이 더 위면 왼쪽
            iseeu(n+1, cnt+3, 4)
            return
        elif i < a and j > b:
            iseeu(n+1, cnt+2, 3)
            return
        else:
            iseeu(n+1, cnt+1, 2)
            return
    elif see == 2: # 아래로 볼 때 대상이 더 오른쪽이면 왼쪽
        if j < b:
            iseeu(n+1, cnt+3, 1)
            return
        elif i > a and j > b:
            iseeu(n+1, cnt+2, 4)
            return
        else:
            iseeu(n+1, cnt+1, 3)
            return
    elif see == 3:
        if i < a: # 좌로 볼 때 대상이 더 아래이면 왼쪽
            iseeu(n+1, cnt+3, 2)
            return
        elif i > a and j < b:
            iseeu(n+1, cnt+2, 1)
            return
        else:
            iseeu(n+1, cnt+1, 4)
            return
    else:
        if j > b:
            iseeu(n+1, cnt+3, 3)
            return
        elif i < a and j < b:
            iseeu(n+1, cnt+2, 2)
            return
        else:
            iseeu(n+1, cnt+1, 1)
            return

    pass


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    target = [(0,0)]
    for w in range(1, 11):
        for i in range(N):
            for j in range(N):
                if arr[i][j] == w:
                    target.append((i,j))

    final = len(target) - 1
    iseeu(0, 0, 1)