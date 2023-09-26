import sys
input = sys.stdin.readline

def act(A, B):
    value = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                value[i][j] += (A[i][k] * B[k][j])
                value[i][j] %= 1000
    return value

def sect(matrix, m):
    if m == 1:
        return matrix

    if m % 2 == 0:
        half = sect(matrix, m // 2)
        return act(half, half)
    else:
        half = sect(matrix, (m - 1) // 2)
        return act(matrix, act(half, half))

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = sect(arr, M)

for _ in result:
    print(*[i%1000 for i in _])