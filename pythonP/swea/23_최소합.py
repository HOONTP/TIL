dij = [(1,0), (0,1)]
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = [[999999999]*N for _ in range(N)]
    lst[0][0] = arr[0][0]
    for i in range(N):
        for j in range(N):
            for k in dij:
                ni = i + k[0]
                nj = j + k[1]
                if ni < N and nj < N:
                    mid = lst[i][j] + arr[ni][nj]
                    if mid < lst[ni][nj]:
                        lst[ni][nj] = mid
    print(f'#{tc}', lst[-1][-1])