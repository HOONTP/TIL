T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    mn = lst[0]
    mn_i = 0
    mx = lst[0]
    mx_i = 0

    for i in range(N):
        if lst[i] < mn:
            mn = lst[i]
            mn_i = i
        if lst[i] >= mx:
            mx = lst[i]
            mx_i = i

    print(f'#{tc} {abs(mx_i-mn_i)}')