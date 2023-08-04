dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for t in range(1, int(input()) + 1):
    N = int(input())
    MAP = [[0] * N for _ in range(N)]

    i, j, number, direct = 0, 0, 1, 0

    MAP[i][j] = number
    number += 1

    while number <= N * N:
        ni = i + dx[direct]
        nj = j + dy[direct]

        if 0 <= ni < N and 0 <= nj < N and MAP[ni][nj] == 0:
            #맵안에 존재하면서, 갈 수 있는경우만
            i = ni
            j = nj
            MAP[i][j] = number
            number += 1
        else:
            direct = (direct + 1) % 4
            #방향에서 들어갈 수 있는 조합 4가지 -> 오른쪽 0, 하향1, 왼쪽 2 상향 3
            # 1 % 4, = 1  2 % 4, = 2 3 % 4 = 3 4 % 4 = 0

    print(f'#{t}')
    #1
    # for i in range(N):
    #     for j in range(N):
    #         print(MAP[i][j], end =" ")
    #     print()


    #2
    # for i in range(N):
    #     print(*MAP[i])

    #3
    for M in MAP:
        print(*M)