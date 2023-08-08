T = int(input())

for tc in range(1, T+1):
    long, short = input().split()
    N = len(long)
    M = len(short)

    cnt = 0
    i = 0

    result = N - (M-1)*long.count(short)
    print(f'#{tc}', result)

    # long = long.replace(short, '1')
    # print(f'#{tc}', len(long))
