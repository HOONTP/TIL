import sys
input = sys.stdin.readline

def backT(visted):
    if len(visted) == M:
        print(*visted)
        return

    for i in lst:
        if i not in visted:
            visted.append(i)
            backT(visted)
            visted.pop()



N, M = map(int, input().split())

lst = list(map(int, input().split()))
visted = []

lst.sort()

backT(visted)
