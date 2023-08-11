T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    mx_val = 0
    total = []
    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
            elif cnt > 1 and mx_val < cnt:
                mx_val = cnt
                cnt = 0
            else:
                cnt = 0
        if cnt > 1 and mx_val < cnt:
            mx_val = cnt

    for j in range(M):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
            elif cnt > 1 and mx_val < cnt:
                mx_val = cnt
                cnt = 0
            else:
                cnt = 0
        if cnt > 1 and mx_val < cnt:
            mx_val = cnt
    print(f'#{tc}', mx_val)
