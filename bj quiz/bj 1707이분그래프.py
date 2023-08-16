import sys
input = sys.stdin.readline
import pprint

def dfs(arr, n):
    global result
    # print(n)
    stack = []
    stack.append(n)
    visted[n] = 1
    while stack:
        # print(stack)
        # print(visted)
        n = stack.pop()
        if visted[n] == 2:#2면 1 1이면 2
            for w in arr[n]:
                if visted[w] == 2:
                    result = -1
                    return
                elif visted[w] == 0:
                    visted[w] = 1
                    stack.append(w)

        elif visted[n] == 1:
            for w in arr[n]:
                if visted[w] == 1:
                    result = -1
                    return
                elif visted[w] == 0:
                    visted[w] = 2
                    stack.append(w)

T = int(input())

for _ in range(T):
    V, E = map(int, input().split()) # 점 개수, 선 개수

    arr = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    # pprint.pprint(arr)
    visted = [0] * (V + 1)
    result = 0

    for i in range(1, V+1):#연결되지 않은 다른 세계관의 그래프가 있을 수 있음
        if visted[i] != 0:#이미 방문한 적 있는 경우 패스
            continue
        visted = [0] * (V + 1)#패스했지만 혹시모르니 리셋
        dfs(arr, i)
        if result == -1:
            print('NO')
            break
    else:
        print('YES')