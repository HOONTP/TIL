from collections import deque
import sys
input = sys.stdin.readline

di = [-1,0,1,0]
dj = [0,1,0,-1]
def diff(zero):
    n = len(zero)
    print(n)
    for i in range(1<<n):
        get_ = []
        for j in range(n):
            if i & (1<<j):
                get_.append(zero[j])
            if len(get_) > 3:
                continue
        if len(get_) == 3:
            one_lst.append(get_)
    return

def bfs(S, arr):
    global mx_val

    q = deque()
    q.append(S)

    while q:
        n = q.popleft()
        for k in range(4):
            ni = n[0] + di[k]
            nj = n[1] + dj[k]
            if 0<= ni <N and 0<= nj <M and arr[ni][nj] == 0:
                arr[ni][nj] = 2
                q.append((ni,nj))
    return arr

def birus(arr):
    global mx_val

    for t in two_lst:
        arr = bfs(t, arr)
        print(arr)
    zero_sums = 0
    for check in range(N):
        zero_sums += arr[check].count(0)

    return zero_sums

N, M = map(int, input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
print(arr)
zero_lst = []
two_lst = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            zero_lst.append((i, j))
        elif arr[i][j] == 2:
            two_lst.append((i, j))
one_lst = []

print('a')

diff(zero_lst)

print('a')

print(one_lst)

mx_val = 0

lst = [a for a in arr]
for w in one_lst:
    for o in w:
        arr[o[0]][o[1]] = 1
    zero_sums = birus(arr)
    if mx_val < zero_sums:
        mx_val = zero_sums
    for o in w:
        arr[o[0]][o[1]] = 0

print(mx_val)