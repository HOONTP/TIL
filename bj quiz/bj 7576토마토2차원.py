from collections import deque
import sys
input = sys.stdin.readline

di = [-1,0,1,0]
dj = [0,1,0,-1]
#전체 수를 찾으려면 dfs
#번지는 회수를 찾으려면 bfs

def bfs(arr, lst):
    q = deque()
    result = [0]#반례 조심하자. 한 번도 시행 안할 때 0 출력.
    for i in lst:
        q.append(i)

    while q:
        n = q.popleft()#i,j,cnt
        for k in range(4):
            ni = n[0] + di[k]
            nj = n[1] + dj[k]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0:
                q.append([ni, nj, n[2]+1])
                arr[ni][nj] = 1
                result.append(n[2]+1)
    for i in arr:
        if 0 in i:
            print(-1)
            return
    print(max(result))#만약 이렇게 안하고 max값을 갱신하는 형식으로 했다면 에러 안났을지도

M, N = map(int, input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
lst = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            lst.append([i,j,0])

bfs(arr, lst)