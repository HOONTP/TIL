import sys
input = sys.stdin.readline

def backT(visted, index):
    if len(visted) == M:
        result.append([i for i in visted])
        return

    for i in range(N):
        if i not in index:
            visted.append(lst[i])
            index.append(i)
            backT(visted, index)
            visted.pop()
            index.pop()



N, M = map(int, input().split())

lst = list(map(int, input().split()))
visted = []
index = []
result = []
lst.sort()

backT(visted, index)

print(result)
result = set(i for i in result)
# result = sorted(result)

print(result)