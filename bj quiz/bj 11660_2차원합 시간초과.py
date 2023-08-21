import sys
input = sys.stdin.readline
'''
time over
'''
N, M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for _ in range(M):
    x1, y1, x2, y2 = map(int,input().split())

    dx = x2 - x1 + 1
    dy = y2 - y1 + 1
    sums = 0
    i = x1 - 1
    j = y1 - 1
    for k in range(dx):
        for l in range(dy):
            if 0 <= i+k < N and 0 <= j+l < N:
                sums += arr[i+k][j+l]
    print(sums)