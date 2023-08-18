T = 10

di = [-1,0,1,0]
dj = [0,1,0,-1]

def bfs(arr, S):
    que = []
    que.append(S)
    arr[S[0]][S[1]] = '1'

    while que:
        n = que.pop(0)
        for k in range(4):
            ni = n[0] + di[k]
            nj = n[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == '0':
                    que.append([ni, nj])
                    arr[ni][nj] = '1'
                elif arr[ni][nj] == '3':#3이면 탈출
                    return 1
    return 0

for tc in range(1, T + 1):
    input()
    N = 16
    arr = [list(input()) for _ in range(16)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                S = (i, j)

    result = bfs(arr, S)
    print(f'#{tc}', result)