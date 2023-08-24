T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    S = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                S.append((i,j))

    sums = 0
    for s in S:
        for p in range(1, N):
            ni = s[0] - p
            nj = s[1]
            if 0<= ni:
                if arr[ni][nj] == 1:
                    sums += 1
                    break
                elif arr[ni][nj] == 2:
                    break
    print(f'#{tc}', sums)
