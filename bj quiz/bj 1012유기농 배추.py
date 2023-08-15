import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0]*(M) for _ in range(N)]

    for _ in range(K):
        a, b = map(int, input().split())
        arr[b][a] = 1

    result = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                stack = [[i, j]]
                result += 1
                while stack:
                    n = stack.pop()
                    if arr[n[0]][n[1]] == 1:
                        arr[n[0]][n[1]] = 0
                        for k in range(4):
                            ni = n[0] + di[k]
                            nj = n[1] + dj[k]
                            if 0 <= ni < N and 0 <= nj < M:
                                if arr[ni][nj] == 1:
                                    stack.append([ni, nj])
    print(result)