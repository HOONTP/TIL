import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000000)
di = [-1,1,0,0]
dj = [0,0,-1,1]

def backT(x, y, visted):
    global cnt

    if x == M-1 and y == N-1:
        for i in visted:
            can_lst[i[0]][i[1]] += 1
        cnt += 1
        return
    if can_lst[x][y] > 0:
        for i in visted:
            can_lst[i[0]][i[1]] = can_lst[x][y]
        cnt += can_lst[x][y]
        return

    for k in range(4):
        ni = x + di[k]
        nj = y + dj[k]
        if 0<=ni<M and 0<=nj<N and arr[ni][nj] < arr[x][y] and (ni,nj) not in visted:
            visted.add((ni,nj))
            backT(ni, nj, visted)
            visted.remove((ni, nj))

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
can_lst = [[0]*N for _ in range(M)]

cnt = 0
backT(0,0,{(0,0)})
print(cnt)