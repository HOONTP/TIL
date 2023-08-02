T = int(input())

for tc in range(1, T+1):
    N = int(input())
    red_lst = [[0]*10 for _ in range(10)]
    blue_lst = [[0]*10 for _ in range(10)]
    for _ in range(N):
        draw = list(map(int, input().split()))

        if draw[-1] == 1:
            for i in range(draw[0], draw[2]+1):
                for j in range(draw[1], draw[3]+1):
                    red_lst[i][j] = 1
        else:
            for i in range(draw[0], draw[2]+1):
                for j in range(draw[1], draw[3]+1):
                    blue_lst[i][j] = 1
    ans_lst = [[red_lst[i][j]+blue_lst[i][j] for j in range(10)] for i in range(10)]
    cnt = 0
    for i in range(10):
        for j in range(10):
            if ans_lst[i][j] == 2:
                cnt += 1
    print(f'#{tc} {cnt}')