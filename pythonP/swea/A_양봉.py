di = [-1, 0, 1, 1, 1, 0] # 홀수 열
dj = [0, 1, 1, 0, -1, -1]

Di = [-1, -1, 0, 1, 0, -1] # 짝수 열
Dj = [0, 1, 1, 0, -1, -1]

T = int(input())

def backT(get, sums, cnt):
    n = get[-1]#마지막 선택 좌표

    if n[1] % 2 == 1:
        for k in range(6):
            ni = n[0] + di[k]
            nj = n[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < M and [ni, nj] not in get:
                if cnt <= 2:
                    get.append([ni, nj])
                    backT(get, sums+arr[ni][nj], cnt+1)
                    get.pop()
                elif cnt == 3:
                    result.append(sums+arr[ni][nj])
    else:
        for k in range(6):
            ni = n[0] + Di[k]
            nj = n[1] + Dj[k]
            if 0 <= ni < N and 0 <= nj < M and [ni, nj] not in get:
                if cnt <= 2:
                    get.append([ni, nj])
                    backT(get, sums+arr[ni][nj], cnt+1)
                    get.pop()
                elif cnt == 3:
                    result.append(sums+arr[ni][nj])

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    result = []
    for i in range(N):
        for j in range(M):
            G = [[i, j]]
            backT(G, arr[i][j], 1)
            one_sum = arr[i][j]
            two_sum = arr[i][j]
            if j % 2 == 1:
                for l in range(3):
                    ni = i+di[l*2]
                    nj = j+dj[l*2]
                    Ni = i+di[l*2+1]
                    Nj = j+dj[l*2+1]
                    if 0<= ni < N and 0<= nj < M:
                        one_sum += arr[ni][nj]
                    if 0<= Ni < N and 0<= Nj < M:
                        two_sum += arr[Ni][Nj]
            else:
                for l in range(3):
                    ni = i + Di[l * 2]
                    nj = j + Dj[l * 2]
                    Ni = i + Di[l * 2 + 1]
                    Nj = j + Dj[l * 2 + 1]
                    if 0 <= ni < N and 0 <= nj < M:
                        one_sum += arr[ni][nj]
                    if 0 <= Ni < N and 0 <= Nj < M:
                        two_sum += arr[Ni][Nj]
            result.append(one_sum)
            result.append(two_sum)

    print(f'#{tc}', max(result))