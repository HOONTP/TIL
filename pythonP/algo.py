import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = []

for _ in range(N):
    lst.append(int(input()))

sums = 0
for i in range(N-1,-1,-1):
    if K // lst[i]:
        sums += K // lst[i]
        K = K % lst[i]

print(sums)