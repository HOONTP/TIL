import sys
input = sys.stdin.readline

def backT(visted, n):
    if len(visted) == M:
        result.append(' '.join(str(i) for i in sorted(visted)))
        return

    for i in range(N):
        if i > n:
        visted.append(lst[i])
        backT(visted, i)
        visted.pop()



N, M = map(int, input().split())

lst = list(map(int, input().split()))
visted = []
result = []

lst.sort()
backT(visted, 0)

result = set(result)
result = sorted(result)
for k in result:
    print(k)