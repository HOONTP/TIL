import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
check_lst = list(map(int, input().split()))
in_lst = list(map(int, input().split()))
M = int(input())
go_lst = list(map(int, input().split()))

target = []
for i in range(N):
    if check_lst[i] == 0:
        target.append(in_lst[i])

target.reverse()
target.extend(go_lst)

for j in range(M):
    print(target[j], end=' ')