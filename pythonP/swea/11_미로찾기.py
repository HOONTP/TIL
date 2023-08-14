T = int(input())

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def find(arr, S):
    stack = [S]
    visted = []
    while stack:
        # print(stack)
        # print(visted)
        start = stack.pop()
        visted.append(start)
        for k in range(4):
            ni = start[0] + di[k]
            nj = start[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < N and [ni, nj] not in visted:
                if arr[ni][nj] == '2':
                    return 1
                elif arr[ni][nj] == '0':
                    stack.append([ni, nj])
    return 0

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '3':
                S = [i, j]

    result = find(arr, S)
    print(f'#{tc}', result)