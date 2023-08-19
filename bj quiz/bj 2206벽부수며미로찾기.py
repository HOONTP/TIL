from collections import deque
import sys
input = sys.stdin.readline
'''
까먹지 말자
1. if 문에서 범위 + 이미 밟은 단계 조건.
1-2. 밟은 곳 처리
2. 종료조건
'''
'''벽부이
1번만 깰 수 있으니 그냥 힘을 1 주고 돌리는게 좋을 것 같음.# i , j , p , count
중간에 힘 없는애가 밟은 코스를 힘 있는 애가 밟지 못함. 와 이거를 어떻게 생각해내야되지?
#
시간 훨씬 짧은 사람들 있는거 보면 좀 더 획기적인 방법이 있는 것 같음.
'''
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
def bfs(arr):
    q = deque()
    q.append((0, 0, 1, 1))
    #visted 대신 0을 -1로 바꾸자

    while q:
        n = q.popleft()#i, j, pw, cnt
        if [n[0], n[1]] == [N - 1, M - 1]:# 웬만하면 여기 넣자.
            #for문에서 미리 거르면 시간을 좀 아낄 수 있긴한데,, 시작 = 끝의 경우를 고려 못함.
            print(n[3])
            return
        for k in range(4):
            ni = n[0] + di[k]
            nj = n[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if n[2] == 1:#힘이 있을 때
                    if arr[ni][nj][0] == '1':#1,-2는 1인데 밟은거랑 1
                        q.append((ni, nj, 0, n[3] + 1))
                        arr[ni][nj] = ['-1']
                    elif arr[ni][nj][0] == '0' or arr[ni][nj][0] == '-2':
                        q.append((ni, nj, n[2], n[3] + 1))
                        arr[ni][nj] = ['-1']
                elif n[2] == 0:  # 힘이 없을 때
                    if arr[ni][nj][0] == '0':
                        q.append((ni, nj, 0, n[3]+1))
                        arr[ni][nj] = ['-2']
    print(-1)#못 찾은 경우
    return

N, M = map(int, input().split())
arr = []
for _ in range(N):
    lst = []
    a = input().strip()
    for i in a:
        lst.append(i)
    arr.append(lst)
bfs(arr)