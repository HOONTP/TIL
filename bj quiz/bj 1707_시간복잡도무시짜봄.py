import sys
input = sys.stdin.readline
import pprint

def dfs(arr, n, visted, distance):
    global result
    # print(n)
    if n == i:
        if distance % 2 == 1:
            result = -1
            return
    if visted[n]:
        return
    visted[n] = True
    for w in arr[n]:
        dfs(arr, w, visted, distance+1)
    return


T = int(input())

for _ in range(T):
    V, E = map(int, input().split()) # 점 개수, 선 개수

    arr = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    # pprint.pprint(arr)

    result = 0
    for i in range(1, V+1):
        visted = [0] * (V + 1)
        dfs(arr, i, visted, 0)
        if result == -1:
            break
    if result == -1:
        print('NO')
    else:
        print('YES')