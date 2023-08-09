T = int(input())

for tc in range(1, T+1):
    N = int(input())

    lst = [1, 0]
    result_lst = []

    print(f'#{tc}')
    for n in range(1,N+1):
        i = 0
        wait_lst = [0]
        while i < n:
            result_lst.append(lst[i]+wait_lst[-1])
            wait_lst.append(lst[i])
            i += 1
        print(*result_lst)
        result_lst.append(0)
        lst[:] = result_lst[:]
        result_lst = []