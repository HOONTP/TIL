T = 10

for tc in range(1, T+1):
    N = int(input())
    lst = [input() for _ in range(8)]

    cnt = 0
    for i in range(8):
        for j in range(8):
            check1 = 0
            check2 = 0
            for k in range(N):
                if j+k < 8 and j+(N-1)-k < 8 and lst[i][j+k] == lst[i][j+(N-1)-k]:
                    check1 += 1
                if i+k < 8 and i+(N-1)-k < 8 and lst[i+k][j] == lst[i+(N-1)-k][j]:
                    check2 += 1
            if check2 == N:
                cnt +=1
            if check1 == N:
                cnt +=1
    print(f'#{tc}', cnt)
