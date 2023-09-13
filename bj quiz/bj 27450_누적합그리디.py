import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())

pow = list(map(int, input().split()))
goal = list(map(int, input().split()))

dif = []
for i in range(N):
    if goal[i] - pow[i] > 0:
        dif.append(goal[i] - pow[i])
    else:
        dif.append(0)

q = deque()
multiple = 0
sums = 0
mid_sum = 0
cnt = 0
i = 0
q_check = 0

while i < N:
    A = dif[i] - mid_sum
    if A > 0:
        if A % K == 0:
            multiple = A // K
        else:
            multiple = A // K + 1
    else:
        multiple = 0

    if q_check:
        cnt -= q.popleft()
    else:
        if len(q) == K - 1:
            q_check = 1

    sums += multiple
    q.append(multiple)
    cnt += multiple
    mid_sum += K * multiple
    mid_sum -= cnt
    i += 1

print(sums)