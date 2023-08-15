import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())
M, N, K = map(int, input().split())
arr = [[0]*(M) for _ in range(N)]

for _ in range(K):
    a, b = map(int, input().split())
    arr[b][a] = 1

print(arr)