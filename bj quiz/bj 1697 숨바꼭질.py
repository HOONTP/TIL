from collections import deque
import sys
input = sys.stdin.readline

def bfs(N, K):# 현재 , 목표
    q = deque()
    q.append([N, 0])
    visted = set()
    visted.add(N)
    while q:
        n = q.popleft()
        if n[0] == K:
            print(n[1])
            return

        if 2*n[0] not in visted and n[0] < K:
            q.append([2*n[0], n[1]+1])
            visted.add(2*n[0])
        if n[0]-1 not in visted:
            q.append([n[0]-1, n[1]+1])
            visted.add(n[0]-1)
        if n[0]+1 not in visted:
            q.append([n[0]+1, n[1]+1])
            visted.add(n[0]+1)


N, K = map(int, input().split())

bfs(N, K)