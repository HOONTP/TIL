T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    print(lst)
    row = N
    col = M

    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    max_v = 0

    for i in range(row):
        for j in range(col):
            s = lst[i][j]
            for k in range(4):
                for s_v in range(1, s + 1):
                    ni = i + s_v * di[k]
                    nj = j + s_v * dj[k]
                    if 0 <= ni < row and 0 <= nj < col:
                        print(lst[ni][nj])
                        s += lst[ni][nj]
            print(s)
            print(i,j)
            if max_v < s:
                max_v = s


    print(f'#{tc} {max_v}')