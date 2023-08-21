T = int(input())
for tc in range(1, T+1):
    N = int(input()) + 1
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                a, b = i, j
                break
    dif = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                dif.append((i-a)**2+(j-b)**2)
    mx = max(dif)
    C = 1
    while True:
        if C ** 2 >= mx:
            print(f'#{tc}', C)
            break
        C += 1