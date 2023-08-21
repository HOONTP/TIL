T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = []
    for i in range(N):
        val = 1
        sums = 0
        for j in range(M):
            if arr[i][j] == lst[j]:
                sums += val
                val += 1
            else:
                val = 1
        result.append(sums)

    print(f'#{tc}', max(result)-min(result))