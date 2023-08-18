import sys
input = sys.stdin.readline

def backT(visted, index):
    if len(visted) == M:
        result.add(tuple(visted))#왜 튜플만 되는겨 여튼 튜플만 set에 가능
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
result = set()
lst.sort()

backT(visted, index)
result = sorted(result) #set는 순서가 없단다 친구야
for _ in result:
    print(*_)