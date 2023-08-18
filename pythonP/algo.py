import sys
input = sys.stdin.readline

def backT(visted, n):
    if len(visted) == M:
        result.add(tuple(visted))#왜 튜플만 되는겨 여튼 튜플만 set에 가능
        return

    for i in range(N):
        if i >= n:
            visted.append(lst[i])
            backT(visted, i)
            visted.pop()

N, M = map(int, input().split())

lst = list(map(int, input().split()))
visted = []
result = set()
lst.sort()

backT(visted, 0)
result = sorted(result) #set는 순서가 없단다 친구야
for _ in result:
    print(*_)