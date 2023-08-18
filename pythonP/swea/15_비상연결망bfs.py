T = 10

def bfs(arr, S):
    q = []
    visted = [0]*(101)
    q.append([S, 0])
    visted[S] = 1
    while q:
        n = q.pop(0)#n[0] = node, n[1] = cnt / 0안쓰고 뻘짓함 하 하
        for w in arr[n[0]]:
            if visted[w] != 1:
                # print(n, w) 오류 잡기 좋은듯
                q.append([w, n[1]+1])
                result.append([w, n[1]+1])
                visted[w] = 1
    return


for tc in range(1, T+1):
    N, S = map(int,input().split())
    arr = [[] for _ in range(101)]
    result = []
    lst = list(map(int, input().split()))

    for i in range(0, N, 2):
        arr[lst[i]].append(lst[i+1])
    bfs(arr, S)

    result.sort(key = lambda x : (x[1], x[0]))

    print(f'#{tc}', result[-1][0])