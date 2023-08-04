T = int(input())

def search(t_page, sr_page):
    s_point = 1
    end_point = t_page
    cnt = 0
    mid_point = (s_point + t_page) // 2
    while mid_point <= end_point: #start <= end로 해야하는듯?
        if mid_point == sr_page:
            return cnt
        if mid_point < sr_page:
            s_point = mid_point # 문제에서는 +- 1을 안해서 1회 이상 더 늦게 찾는 경우가 발생함
            cnt += 1
        else:
            end_point = mid_point
            cnt += 1
        mid_point = (s_point + end_point) // 2

for tc in range(1, T+1):
    N, A, B = map(int, input().split())

    a_cnt = search(N, A)
    b_cnt = search(N, B)
    result = 0
    if a_cnt < b_cnt:
        result = 'A'
    elif a_cnt > b_cnt:
        result = 'B'
    print(f'#{tc} {result}')


