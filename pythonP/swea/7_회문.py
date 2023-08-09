T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    lst = [list(input()) for _ in range(N)]

    # print(lst)

    for i in range(N):
        for j in range(N):
            j_cnt = 0
            i_cnt = 0
            for k in range(M):
                if j+M-1 < N:
                    if lst[i][j+k] == lst[i][j+M-1-k]:
                        j_cnt += 1
                if i+M-1 < N:
                    if lst[i+k][j] == lst[i+M-1-k][j]:
                        i_cnt += 1
            if j_cnt == M:
                result = lst[i][j:j+M]
                print(f'#{tc}', ''.join(result))
                break
            elif i_cnt == M:
                print(f'#{tc}', end=' ')
                for l in range(M):
                    print(lst[i+l][j], end='')
                print()
                break

    # for col in range(8 - N + 1):
    #     for row in range(8):
    #         palindrome = ''
    #         for cnt in range(N):
    #             palindrome += MAP[col + cnt][row]
    #         if palindrome == palindrome[::-1]:
    #             result += 1


    # zip(*lst) <= 90도 회전된다. zip은 같은 index끼리 합친다.

    # for t in range(1, 11):
    #     N = int(input())
    #     MAP = list(input() for _ in range(8))
    #     MAP += zip(*MAP)
    #     result = 0
    #
    #     for m in MAP:
    #         for i in range(8 - N + 1):
    #             if m[i: i + N] == m[i: i + N][::-1]:
    #                 result += 1
    #
    #     print(f'#{t} {result}')