import sys
input = sys.stdin.readline

def backT(visted, j):
    if len(visted) == M:
        print(*visted)
        return
    for i in range(j, N):
        if lst[i] not in visted:
            visted.append(lst[i])
            backT(visted, lst[i])#lst[i]인 이유 index가 한칸씩 -1 이니깐.
            visted.pop()

N, M = map(int, input().split())
lst = list(range(1, N+1))

visted = []
backT(visted, 0)