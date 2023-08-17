import sys
input = sys.stdin.readline

def backT(visted):
    if len(visted) == M:
        # print(visted)
        result.append(' '.join(str(i) for i in sorted(visted)))
        return
    for i in lst:
        if i not in visted:
            visted.append(i)
            backT(visted)
            visted.pop()

N, M = map(int, input().split())
lst = list(range(1, N+1))

visted = []
result = []
backT(visted)

result = set(result)
result = sorted(result)# 이거 안해주면 pypy는 통과 python은  fail 뜬다.
for i in result:
    print(i)