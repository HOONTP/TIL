from collections import deque
import sys
input = sys.stdin.readline

di = [-1,0,1,0]
dj = [0,1,0,-1]

def bfs(arr, E):
    q = deque()
    q.append([0,0,1])
    arr[0][0] = '0'
    while q:
        n = q.popleft()
        for k in range(4):
            ni = n[0] + di[k]
            nj = n[1] + dj[k]
            if ni == E[0] and nj == E[1]:
                return n[2]+1
            elif 0<=ni<N and 0<=nj<M and arr[ni][nj] == '1':
                q.append([ni, nj, n[2]+1])
                arr[ni][nj] = '0'

    return 0

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
E = [N-1, M-1]

result = bfs(arr, E)
print(result)