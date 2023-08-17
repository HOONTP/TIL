import sys
input = sys.stdin.readline
import pprint

def backT(visted):
    global result
    if len(visted) == M:
        print(*visted)
        return
    for i in lst:
        if i not in visted:
            visted.append(i)
            backT(visted)
            visted.pop()

N, M = map(int, input().split())
lst = list(range(1,N+1))

visted = []
backT(visted)