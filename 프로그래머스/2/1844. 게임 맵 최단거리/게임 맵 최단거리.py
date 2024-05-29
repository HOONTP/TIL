dij = [(-1, 0), (0, 1), (1, 0), (0, -1)]
from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    q = deque()
    q.append([(0,0), 1])
    maps[0][0] == 0
    answer = -1

    while q:
        point, cnt = q.popleft()
        if point == (n-1,m-1):
            return cnt
        for dxy in dij:
        
            dx, dy = dxy
            x = point[0] + dx
            y = point[1] + dy

            if 0<= x < n and 0<= y <m and maps[x][y] == 1:
                q.append([(x,y), cnt+1])
                maps[x][y] = 0

    return answer