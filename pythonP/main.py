import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000000)
di = [-1,1,0,0]
dj = [0,0,-1,1]

def dfs(x,y):
    stack = []
    stack.append((x,y))

# 이미 1로 처리된 지점을 밟는 순간 돌아가고? 1을 밟는 케이스 기준 교차점에 +1을 해주고 그 값으로 또 돌아가면서 +1해주는 식이 될까?
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
can_lst = [[0]*N for _ in range(M)]

cnt = 0
backT(0,0,{(0,0)})
print(cnt)