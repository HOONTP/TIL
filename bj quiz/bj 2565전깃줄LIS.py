import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

lst.sort()
result = [1] * N

for i in range(N):
    for j in range(i):
        if lst[i][1] > lst[j][1]:
            result[i] = max(result[i], result[j] + 1)


print(N-max(result))