T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    lst = [list(input()) for _ in range(N)]

    # print(lst)

    for i in range(N):
        for j in range(N):
            j_cnt = 0
            i_cnt = 0
            for k in range(M):
                if j+M-1 < N:
                    if lst[i][j+k] == lst[i][j+M-1-k]:
                        j_cnt += 1
                if i+M-1 < N:
                    if lst[i+k][j] == lst[i+M-1-k][j]:
                        i_cnt += 1
            if j_cnt == M:
                result = lst[i][j:j+M]
                print(f'#{tc}', ''.join(result))
                break
            elif i_cnt == M:
                print(f'#{tc}', end=' ')
                for l in range(M):
                    print(lst[i+l][j], end='')
                print()
                break