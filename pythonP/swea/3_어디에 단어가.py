T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    md_lst = [list(map(int, input().split()))for _ in range(N)]
    cnt = 0

    for i in range(N):
        m_cnt = 0 # 초기화 유의하기
        for j in range(N):
            if md_lst[i][j] == 1:
                m_cnt += 1
                if m_cnt == M:
                    if j+1 < N and md_lst[i][j+1] == 0:
                        cnt += 1
                        m_cnt = 0 # 초기화 유의하기
                    elif j+1 == N:
                        cnt += 1
                        m_cnt = 0 # 초기화 유의하기
            else:
                m_cnt = 0 # 초기화 유의하기


    for j in range(N):
        m_cnt = 0
        for i in range(N):
            if md_lst[i][j] == 1:
                m_cnt += 1
                if m_cnt == M:
                    if i+1 < N and md_lst[i+1][j] == 0:
                        cnt += 1
                        m_cnt = 0
                    elif i+1 == N:
                        cnt += 1
                        m_cnt = 0
            else:
                m_cnt = 0

    print(f'#{tc} {cnt}')