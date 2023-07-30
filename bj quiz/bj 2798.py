import sys
import time
input = sys.stdin.readline

N, M = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()

aver = M//3
i = 1
print(aver)
print(i)
print(lst)

con = lst[i-1] + lst[i] + lst[i+1]
while lst[i] + lst[i+1] + lst[i+2] <= M:
    con = lst[i] + lst[i+1] + lst[i+2]
    i += 1

print(con)