from collections import deque
import sys
input = sys.stdin.readline

'''
A -> B
*2
+'1'
'''

def bfs(A, B):
    q = deque()
    q.append((A, 1))
    visted = set()
    visted.add(A)

    while q:
        n = q.popleft()
        if n[0] == B:
            print(n[1])
            return
        if n[0]*2 <= B and n[0]*2 not in visted:
            q.append((n[0]*2, n[1]+1))
            visted.add(n[0]*2)
        if int(str(n[0])+'1') <= B and int(str(n[0])+'1') not in visted:
            q.append((int(str(n[0])+'1'), n[1]+1))
            visted.add(int(str(n[0])+'1'))
    print(-1)
    pass


A, B = map(int, input().split())

bfs(A, B)