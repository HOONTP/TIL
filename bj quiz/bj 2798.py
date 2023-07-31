import sys
import time
input = sys.stdin.readline

N, M = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()
lsum = 0
mx = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            lsum = lst[i] + lst[j] + lst[k]
            if lsum <= M and mx < lsum:
                mx = lsum
            if lsum > M:
                break
print(mx)