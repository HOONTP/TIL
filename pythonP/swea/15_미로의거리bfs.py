T = int(input())

di = [-1,0,1,0]
dj = [0,1,0,-1]

def bfs(arr, S):
    que = []
    que.append(S)
    arr[S[0]][S[1]] = 1

    while que:
        n = que.pop(0)#튜플
        for k in range(4):
            ni = n[0] + di[k]
            nj = n[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 0:
                    que.append([ni, nj, n[2]+1])#1씩 추가
                    arr[ni][nj] = 1
                elif arr[ni][nj] == 3:#3이면 탈출
                    return n[2]
    return 0

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                S = (i, j, 0)
    result = bfs(arr, S)
    print(f'#{tc}', result)