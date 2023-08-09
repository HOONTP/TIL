T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    sell = 0
    mx_val = lst[-1]

    for i in range(N-1, -1, -1):
        if lst[i] < mx_val:
            sell = sell + mx_val - lst[i]
        else:
            mx_val = lst[i]

    print(f'#{tc}', sell)