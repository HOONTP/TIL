T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    cnt = 1
    mx_val = 0
    for i in range(N - 1):
        if lst[i] + 1 == lst[i + 1]:
            cnt += 1
        else:
            if mx_val < cnt:
                mx_val = cnt
            cnt = 1
    if mx_val < cnt:
        mx_val = cnt
    print(f'#{tc}', mx_val)