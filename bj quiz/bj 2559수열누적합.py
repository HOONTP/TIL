import sys
input = sys.stdin.readline

N, K = map(int, input().split())

lst = list(map(int, input().split()))


for i in range(1, N):
    lst[i] = lst[i] + lst[i-1]


mx = lst[K-1]# index헷갈리지 말자
for i in range(N-K):
    if mx < lst[i+K] - lst[i]:
        mx =lst[i+K] - lst[i]
print(mx)