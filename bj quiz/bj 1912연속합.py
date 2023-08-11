import sys
input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))
mx_val = -1000
sums_l = 0
for i in lst:
    sums_l += i
    if mx_val < sums_l:
        mx_val = sums_l
    if sums_l < 0:
        sums_l = 0

print(mx_val)