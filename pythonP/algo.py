import sys
input = sys.stdin.readline

N = int(input())

lst = [int(input()) for _ in range(N)]

result = [0]*N
result[0] = lst[0]

for i in range(1, N):
    if i-3 >= 0:
        new_sum = result[i-3]+lst[i-1]+lst[i]
    else:
        new_sum = lst[i-1]+lst[i]
    if i-2 >= 0:
        sec_sum = result[i-2] + lst[i]
    else:
        sec_sum = lst[i]

    result[i] = max(result[i-1], new_sum, sec_sum)
print(result[-1])