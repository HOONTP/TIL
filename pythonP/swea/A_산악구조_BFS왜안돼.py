"""
터널 없이 경로마다 최소값 구한 다음
터널을 탄 경우를 추가하여 다시 구해야하나? => 그 다음 경로들의 최소값이 모두 변경된다.

한 위치에 여러 개의 터널이 뚫려 있는 경우가 있음.
"""

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

def bfs(S):
    n = S

    for k in range(4):
        ni = n[0] + di[k]
        nj = n[1] + dj[k]
        if 0<= ni <N and 0<= nj <N:
            if arr[n[0]][n[1]] > arr[ni][nj]:
                gas = (arr[n[0]][n[1]] - arr[ni][nj]) * 2 + lst[ni][nj]
            elif arr[n[0]][n[1]] == arr[ni][nj]:
                gas = lst[ni][nj] + 1
            else:
                gas = lst[ni][nj]
            if gas < lst[n[0]][n[1]]:
                lst[n[0]][n[1]] = gas

    if dict_lst[n[0]][n[1]]:
        for A in dict_lst[n[0]][n[1]]:
            if lst[A[0]][A[1]] > A[2] + lst[n[0]][n[1]]:
                lst[A[0]][A[1]] = A[2] + lst[n[0]][n[1]]

def real_bfs():
    q = []
    q.append((0, 0))
    visted = []
    visted.append((0, 0))

    while q:
        n = q.pop(0)
        bfs((n[0], n[1]))
        for k in range(4):
            ni = n[0] + di[k]
            nj = n[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in visted:
                q.append((ni, nj))
                visted.append((ni, nj))

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dict_lst = [[[] for _ in range(N)] for _ in range(N)]
    lst = [[999999999]*N for _ in range(N)]
    lst[0][0] = 0
    for _ in range(M):
        a, b, c, d, E = map(int, input().split())
        dict_lst[a-1][b-1].append((c-1, d-1, E))
        dict_lst[c-1][d-1].append((a-1, b-1, E))
    # for _ in range(4):
    #     for i in range(N):
    #         for j in range(N):
    #             bfs((i, j))
    real_bfs()
    real_bfs()
    print(f'#{tc}', lst[-1][-1])