T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    #최고값 탐색과 최저값 탐색을 번갈아하면 되지 않을까?
    mx_num = 0
    mn_num = 101
    new_lst = []
    for i in range(10):
        if i % 2 == 0:# max
            for j in range(i, N):
                if mx_num < lst[j]:
                    mx_num = lst[j]
                    mx_idx = j
            lst[i], lst[mx_idx] = lst[mx_idx], lst[i]
            mx_num = 0
        else:
            for k in range(i, N):
                if mn_num > lst[k]:
                    mn_num = lst[k]
                    mn_idx = k
            lst[i], lst[mn_idx] = lst[mn_idx], lst[i]
            mn_num = 101

    print(f'#{tc}', *lst[:10])