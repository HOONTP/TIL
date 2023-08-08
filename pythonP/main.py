T = int(input())

for tc in range(1, T+1):
    A = input()
    full = input()

    mx_cnt = 0
    mx_alpha = []
    dic_A = {}
    dic_full = {}
    for i in A:
        A_cnt = A.count(i)
        dic_A[i] = A_cnt
        if mx_cnt < A_cnt:
            mx_cnt = A_cnt
            mx_alpha = [i]
        elif mx_cnt == A_cnt:
            mx_alpha.append(i)

    for i in full:
        dic_full[i] = full.count(i)
    set_alpha = set(mx_alpha)

    if len(set_alpha) == 1:
        print(dic_full[mx_alpha[0]])
