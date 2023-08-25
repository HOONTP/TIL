import sys
input = sys.stdin.readline

N, M = map(int, input().split())

lst = list(map(int, input().split()))
for i in range(1, N):
    lst[i] += lst[i-1]

for _ in range(M):
    a, b = map(int,input().split())
    if a == 1:
        print(lst[b-1])
    else:
        print(lst[b-1]-lst[a-2])