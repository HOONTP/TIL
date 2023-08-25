import sys
input = sys.stdin.readline
#15961
N, d, k, c = map(int, input().split())

lst = []
for _ in range(N):
    lst.append(int(input()))

lst = lst*2
mx = 0
# 2n * (k +k) 너무 많다.
for i in range(N*2-(k-1)):
    mid = set(lst[i:i+k])
    if c not in mid:
        sums = len(mid) + 1
    else:
        sums = len(mid)

    if mx < sums:
        mx = sums
    if mx >= k+1:
        break
print(mx)