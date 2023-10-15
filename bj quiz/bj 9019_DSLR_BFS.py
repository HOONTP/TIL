import sys
input = sys.stdin.readline
from collections import deque

def bfs(a):
    q = deque()
    q.append((a, ''))
    visited = [0]*10000

    while q:
        n, ans = q.popleft()
        if n == B:
            return ans
        nstr = str(n).zfill(4)
        Lnum = nstr[1:4] + nstr[0]
        Rnum = nstr[3] + nstr[:3]
        # print(Lnum, Rnum)
        j = 2*n % 10000
        k = (n-1) % 10000
        l = int(Lnum) % 10000
        p = int(Rnum) % 10000
        if visited[j] == 0:
            q.append((j, ans+'D'))
            visited[j] = 1
        if visited[k] == 0:
            q.append((k, ans+'S'))
            visited[k] = 1
        if visited[l] == 0:
            q.append((l, ans+'L'))
            visited[l] = 1
        if visited[p] == 0:
            q.append((p, ans+'R'))
            visited[p] = 1

for _ in range(int(input())):
    A, B = map(int, input().split())

    result = bfs(A)
    print(result)