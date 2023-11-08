import sys
sys.setrecursionlimit(5000) # 기본 값이 2000 언저리라 늘려줘야함.
dij = [(1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')] # [아, 왼, 오, 위]

def solution(n, m, x, y, r, c, k): # i, j, 출발점, 도착점, k는 2500이하 낭비가능한 횟수는 짝수 => k - (도-출)이 홀수면 불가능 하다.
    # d l r u 아 왼 오 위 / 백트래킹이 가장 무난 방향의 우선순위가 있으니 멀어지면 최대 거리가 도착이 불가능할 경우 멈춰버리면 된다. 아에 단축할 방법은 없나? // 해봤자 한칸 씩 가는걸 한 번에 가는거밖에 안되긴한데 ,, 절대 안되네
    def finish(result, x, y, r, c):
        di, dj = abs(x-r), abs(y-c)
        if x < r:
            result += 'd'*di
            if y < c:
                result += 'r'*dj
            else:
                result += 'l'*dj
            return result
        else:
            if y < c:
                result += 'r'*dj
                result += 'u'*di
            else:
                result += 'l'*dj
                result += 'u'*di
            return result

    def backT(result, x, y, r, c, k, n, m):
        # if k == 0 and x == r and y == c:
        #     answer.append(result)
        distance = abs(x-r) + abs(y-c)
        # if k < distance:
        #     return
        if k == distance:
            answer.append(finish(result, x, y, r, c))
            return
        # if k == 0: # finish 안해도 거의 차이 없음
        #     answer.append(result)
        #     return
        else:
            for i, j, w in dij:
                # print(0<x+i<=n, 0<y+j<=m , (abs(x-r+i)+abs(y-c+j)) <= k-1)
                dx, dy = x+i, y+j
                if 0<dx<=n and 0<dy<=m and (abs(dx-r)+abs(dy-c)) <= k-1:
                    backT(result+w, dx, dy, r, c, k-1, n, m)
                    break
        return
    answer = []
    MAP = [[0]*m for _ in range(n)]
    di, dj = abs(x-r), abs(y-c)
    distance = di+dj
    remain = k - distance
    if remain % 2 == 1 or k < distance:
        return "impossible"
    elif k > distance:
        backT('', x, y, r, c, k, n, m)
    else:
        return finish('', x, y, r, c)
    return answer[0]