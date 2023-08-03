T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [[0]*N for _ in range(N)]
    # nums = [i for i in range(1,N**2+1)]
    for n in range(1, N+1):
        lst[0][n-1] = n
    i = N+1
    a, b = 0, N-1

    for k in range(N):
        go_right = 0
        go_left = 0
        while go_left < (N-1-k):
            a += 1 + (-2)*(k % 2)
            lst[a][b] = i
            i += 1
            go_left += 1
        while go_right < (N-1-k): # 2 1
            b += -1 + 2*(k % 2)
            lst[a][b] = i
            i += 1
            go_right += 1

        if i == N**2:
            break
    print(f'#{tc}')
    for _ in lst:
        print(*_)