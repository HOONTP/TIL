import sys
sys.setrecursionlimit(5000) # 기본 값이 2000 언저리라 늘려줘야함.
dij = [(1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')] # [아, 왼, 오, 위]
# 이게 조금 더 느림
def solution(n, m, x, y, r, c, k):
    def backT(result, x, y, r, c, k, n, m):
        distance = abs(x-r) + abs(y-c)
        if k == 0: # finish 안해도 거의 차이 없음
            answer.append(result)
            return
        else:
            for i, j, w in dij:
                dx, dy = x+i, y+j
                if 0<dx<=n and 0<dy<=m and (abs(dx-r)+abs(dy-c)) <= k-1:
                    backT(result+w, dx, dy, r, c, k-1, n, m)
                    break
    answer = []
    distance = abs(x-r) + abs(y-c)
    remain = k - distance
    if remain % 2 == 1 or k < distance:
        return "impossible"
    else:
        backT('', x, y, r, c, k, n, m)
    return answer[0]
