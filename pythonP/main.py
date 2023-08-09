T = int(input())

for tc in range(1, T+1):
    A = input()
    full = input()

    mx_cnt = 0
    mx_alpha = set(A)
    dic_full = {}

    for i in full:
        dic_full[i] = full.count(i)

    mx_result = 0
    for j in mx_alpha:
        if mx_result < dic_full[j]:
            mx_result = dic_full[j]
    print(f'#{tc}', mx_result)

    F = max(dic_full.values())
    print(F)

