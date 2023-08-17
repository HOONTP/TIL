for tc in range(1, 11):
    input()
    lst = list(map(int, input().split()))

    a = lst.index(min(lst))
    A = lst[a] // 15 -1
    for k in range(8):
        lst[k] = lst[k] % A

    i = 0
    j = 1
    while True:
        if i == 8:
            i = 0
        if j == 6:
            j = 1
        if lst[i] <= j:
            lst[i] = 0
            break

        lst[i] -= j
        i += 1
        j += 1

    result = lst[i+1:] + lst[:i+1]
    print(f'#{tc}', *result)