import sys
input = sys.stdin.readline
import math

N, M = map(int, input().split())
lst = list(map(int, input().split()))

arr = [0]*(N+1)
arr[1] = lst[0] % M
for i in range(2, N+1):
    arr[i] = (arr[i-1]+lst[i-1]) % M

count_lst = [0]*M
for k in range(1, N+1):
    count_lst[arr[k]] += 1
sums = count_lst[0] + math.comb(count_lst[0], 2)
for l in range(1, M):
    if count_lst[l] > 1:
        sums += math.comb(count_lst[l], 2)
print(sums)

#
# cnt = 0
# for i in range(1, N+1):
#     for j in range(i):
#         if (arr[i] - arr[j]) % M == 0:
#             cnt += 1