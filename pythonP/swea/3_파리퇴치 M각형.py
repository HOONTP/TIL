T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 0, 1, 1]
    dj = [0, 1, 0, 1]
    md_s = 0
    mx_s = lst[0][0]
    for i in range(N):
        for j in range(N):
            for k in range(M):
                for l in range(M):
                    if i+k < N and j+l < N:
                        md_s += lst[i+k][j+l]
            if mx_s < md_s:
                mx_s = md_s
            md_s = 0

    print(f'#{tc} {mx_s}')