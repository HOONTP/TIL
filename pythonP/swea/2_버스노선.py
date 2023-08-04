T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = []
    for ti in range(N):
        A, B = map(int, input().split())
        lst.append((A,B))
    P = int(input())
    result = []
    for _ in range(P):
        C = int(input())
        cnt = 0
        for i in lst:
            if i[0] <= C <= i[1]:
                cnt += 1
        result.append(cnt)

    print(f'#{tc}', *result)