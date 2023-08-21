T = int(input())
#몇 개 인지가 아니라 가능한지라서 가장 먼저 만난 애 기준으로 안되면 불가능 이네.
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    pasw = list(map(int, input().split()))
    result = -1
    j = 0
    for i in lst:
        if pasw[j] == i:
            j += 1
        if j == K:
            result = 1
            break
    if j != K:
        result = 0
    print(f'#{tc}', result)