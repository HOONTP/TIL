T = int(input())

for tc in range(1, T+1):
    N = int(input())

    lst = [0]*5
    num_lst = [2, 3, 5, 7, 11]
    for i in range(5):
        while N % num_lst[i] == 0:
            N = N / num_lst[i]
            lst[i] += 1

    print(f'#{tc}', *lst)