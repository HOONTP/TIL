import sys
input = sys.stdin.readline

def backT(visted):
    if len(visted) == M:
        result.append(' '.join(str(i) for i in sorted(visted)))
        return

    for i in lst:
        visted.append(i)
        backT(visted)
        visted.pop()



N, M = map(int, input().split())

lst = list(map(int, input().split()))
visted = []
result = []

lst.sort()
backT(visted)

result = set(result)
result = sorted(result)
for k in result:
    print(k)