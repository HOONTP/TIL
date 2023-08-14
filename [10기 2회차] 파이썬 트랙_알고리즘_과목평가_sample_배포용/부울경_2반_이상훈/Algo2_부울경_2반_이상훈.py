T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    result = 0
    for pwr in range(1, N+1):
        for i in range(N):
            if pwr*i < N:
                result += lst[pwr*i]

    if result < 0:
        result = 0

    print(f'#{tc}', result)