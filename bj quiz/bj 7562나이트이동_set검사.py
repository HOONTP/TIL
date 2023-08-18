from collections import deque
import sys
input = sys.stdin.readline

di = [-2, -1, 1, 2, 2, 1, -1, -2]
dj = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(S, E):
    q = deque()
    q.append(S)
    visted = set()#이게 큰듯? not in 할 때
    visted.add((S[0],S[1]))
    if [S[0], S[1]] == E:
        print(S[2])
        return
    while q:
        n = q.popleft()# 좌표

        for k in range(8):
            ni = n[0] + di[k]
            nj = n[1] + dj[k]
            if [ni, nj] == E:
                print(n[2]+1)
                return

            if 0<=ni<N and 0<=nj<N and (ni,nj) not in visted:#set으로 하자 tuple로 넣으면 된다.
                q.append([ni,nj,n[2]+1])
                visted.add((ni, nj))


for _ in range(int(input())):
    N = int(input())
    a, b = map(int, input().split())
    E = list(map(int, input().split()))
    S = [a, b, 0]

    bfs(S, E)