T = 10

for tc in range(1, T+1):
    N = int(input())
    md_lst = [list(map(int, input().split()))for _ in range(100)]
    mx_val = md_lst[0][0]
    md_s = 0
    for i in range(100):
        md_s = 0
        for j in range(100):
            md_s += md_lst[i][j]
        if mx_val < md_s:
            mx_val = md_s

    for j in range(100):
        md_s = 0
        for i in range(100):
            md_s += md_lst[i][j]
        if mx_val < md_s:
            mx_val = md_s

    for it in range(2): # 대각선
        md_s = 0
        for ij in range(100):
            md_s += md_lst[ij][ij+(99-2*ij)*it]
        if mx_val < md_s:
            mx_val = md_s

    print(f'#{tc} {mx_val}')