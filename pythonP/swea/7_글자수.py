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

# T = int(input())
#
# for t in range(1, T + 1):
#     str1 = input()
#     str2 = input()
#     dic = {w : str2.count(w) for w in str2 if w in str1 }
#     result = max(dic.values())
#     print(f'#{t} {result}')