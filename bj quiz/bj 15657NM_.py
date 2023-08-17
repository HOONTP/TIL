import sys
input = sys.stdin.readline

def backT(visted, n):
    if len(visted) == M:
        # result.append(' '.join(str(i) for i in sorted(visted)))
        print(*visted)
        return

    for i in range(N):
        if i >= n:
            visted.append(lst[i])
            backT(visted, i)
            visted.pop()



N, M = map(int, input().split())

lst = list(map(int, input().split()))
visted = []

lst.sort()
backT(visted, 0)