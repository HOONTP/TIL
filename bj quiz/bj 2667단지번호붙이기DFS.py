import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N = int(input())
arr = [list(input().strip()) for _ in range(N)]
result = 0
cnt = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1':
            result += 1
            stack = [[i, j]]
            arr[i][j] = '0'
            sums = 0
            while stack:
                n = stack.pop()
                sums += 1
                for k in range(4):
                    ni = n[0] + di[k]
                    nj = n[1] + dj[k]
                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj] == '1':
                            stack.append([ni, nj])
                            arr[ni][nj] = '0'
            cnt.append(sums)
cnt.sort()
print(result)
[print(i) for i in cnt]