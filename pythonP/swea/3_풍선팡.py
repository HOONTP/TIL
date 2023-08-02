T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_lst = []
    for _ in range(N):
        md = list(map(int, input().split()))
        num_lst.append(md)
    print(num_lst)
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    mx_s = 0
    for i in range(N):
        for j in range(M):
            md_s = num_lst[i][j]
            for k in range(4):
                for p in range(1, num_lst[i][j]+1):
                    if 0 <= i+di[k]*p < N and 0 <= j+dj[k]*p < M:
                        md_s += num_lst[i+di[k]*p][j+dj[k]*p]
            if md_s > mx_s:
                mx_s = md_s

    print(f'#{tc} {mx_s}')