import sys
input = sys.stdin.readline

N = int(input())

arr = [list((map(int, input().split()))) for _ in range(N)]
result = [0] * N

for i in range(N-1, -1, -1):
    if arr[i][0] <= N - i:
        if i + arr[i][0] <= N-1:
            first = arr[i][1] + result[i + arr[i][0]]
        else:
            first = arr[i][1]
    else:
        first = 0
    if i+1 <= N-1:
        second = result[i+1]
    else:
        second = 0
    result[i] = max(first, second)
print(max(result))