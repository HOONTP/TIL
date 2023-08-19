from collections import deque
import sys
input = sys.stdin.readline
'''
까먹지 말자
1. if 문에서 범위 + 이미 밟은 단계 조건.
1-2. 밟은 곳 처리
2. 종료조건
'''
def bfs(lst):
    q = deque()
    q.append((1,0))
    lst[1] = 1

    while q:
        n = q.popleft()#num,cnt
        if n[0] == 100:
            print(n[1])
            return

        for w in range(1,7):
            ni = n[0]+w
            if ni < 101 and lst[ni] != 1:
                if ni in jump:
                    q.append((jump[ni], n[1]+1))
                    lst[jump[ni]] = 1
                else:
                    q.append((ni, n[1]+1))
                    lst[ni] = 1
    return

N, M = map(int, input().split())
jump = {}
lst = [0]*101
for _ in range(N+M):
    a, b = map(int, input().split())
    jump[a] = b

# print(jump)

bfs((lst))