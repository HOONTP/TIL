import sys
input = sys.stdin.readline

def dfs(V, E, R):
    global result
    visted = [0] * (V+1)
    stack = []
    visted[R] = 1
    result[R] = 1
    i = 2

    while True:
        for w in E[R]:
            if visted[w] == 0:
                stack.append(R)
                R = w
                visted[R] = 1
                result[R] = i
                i += 1
                break
        else:
            if stack:
                R = stack.pop()
            else:
                break
    return

N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]
result = {}

for __ in range(M):
    A, B = map(int, input().split())
    arr[A].append(B)
    arr[B].append(A) # 이거 안해서 몇분을 쳐다 본거야.?

for i in arr:#왜 시간복잡도 ㅜ
    if len(i) > 1:
        i.sort(reverse=True)

if len(arr[1]) == M:
    print(1)
    for i in arr[1]:
        print(i)
else:
    dfs(N, arr, R)
    for i in range(1, N+1):
        print(result.get(i, 0))