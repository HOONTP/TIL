import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

result_st = [1] * N
result_nd = [0] * N

for i in range(N):
    for j in range(i):
        if lst[i] > lst[j]:
            result_st[i] = max(result_st[i], result_st[j] + 1)
        if lst[N-1-i] > lst[N-1-j]:
            result_nd[N-1-i] = max(result_nd[N-1-i], result_nd[N-1-j] + 1)

result = []
for k in range(N):
    result.append(result_st[k] + result_nd[k])

print(max(result))