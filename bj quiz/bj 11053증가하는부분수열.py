import sys
input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))
result = [1]*N

for i in range(N):
    for j in range(i):
        if lst[i] > lst[j]:
            result[i] = max(result[i], result[j]+1)

print(max(result))