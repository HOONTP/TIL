T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())# 이동거리, 총 거리, 충전기 갯수
    E_lst = list(map(int, input().split()))
    road = [0] * (N+1)

    for i in E_lst: #게임처럼 만들기 or 규칙성 찾기
        road[i] = 1
    cnt = 0
    check_p = 0
    move_p = K
    while move_p < N:
        if check_p == move_p:
            cnt = 0
            break
        if road[move_p] == 1:
            check_p = move_p
            move_p += K
            cnt += 1
        else:
            move_p -= 1

    print(f'#{tc}', cnt)