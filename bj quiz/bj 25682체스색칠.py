import sys
input = sys.stdin.readline

DIJ = [(1,0), (0,1)]

N, M, K = map(int, input().split())

arr = [list(input().strip()) for _ in range(N)]
B_lst = [[0]*(M+1) for _ in range(N+1)]
W_lst = [[0]*(M+1) for _ in range(N+1)]

q = [(1, 1)]
visted = [(1, 1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        if (i + j) % 2 == 0:
            if arr[i-1][j-1] == 'W':
                B_lst[i][j] = B_lst[i - 1][j] + B_lst[i][j - 1] - B_lst[i - 1][j - 1] + 1
                W_lst[i][j] = W_lst[i - 1][j] + W_lst[i][j - 1] - W_lst[i - 1][j - 1]
            else:
                B_lst[i][j] = B_lst[i - 1][j] + B_lst[i][j - 1] - B_lst[i - 1][j - 1]
                W_lst[i][j] = W_lst[i - 1][j] + W_lst[i][j - 1] - W_lst[i - 1][j - 1] + 1
        else:
            if arr[i-1][j-1] == 'B':
                B_lst[i][j] = B_lst[i - 1][j] + B_lst[i][j - 1] - B_lst[i - 1][j - 1] + 1
                W_lst[i][j] = W_lst[i - 1][j] + W_lst[i][j - 1] - W_lst[i - 1][j - 1]
            else:
                B_lst[i][j] = B_lst[i - 1][j] + B_lst[i][j - 1] - B_lst[i - 1][j - 1]
                W_lst[i][j] = W_lst[i - 1][j] + W_lst[i][j - 1] - W_lst[i - 1][j - 1] + 1

mn = 999999999
for i in range(1, N-K+2): #인덱스가 너무 복잡한데,,
    for j in range(1, M-K+2):
        mid_sums = B_lst[i+K-1][j+K-1] - B_lst[i+K-1][j-1] - B_lst[i-1][j+K-1] + B_lst[i-1][j-1]
        if mid_sums < mn:
            mn = mid_sums
        mid_sums = W_lst[i + K - 1][j + K - 1] - W_lst[i + K - 1][j-1] - W_lst[i-1][j + K - 1] + W_lst[i-1][j-1]
        if mid_sums < mn:
            mn = mid_sums

print(mn)