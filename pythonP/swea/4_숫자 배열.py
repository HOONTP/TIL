T = int(input())
for tc in range(1, T+1):
    N = int(input())
    t1 = []
    print(f'#{tc}')
    for abc in range(1, N+1):
        t2 = list(input().split())
        t1.append(t2)
    t3 = []
    for i in range(1, N+1):
        exam1 = ''
        exam2 = ''
        exam3 = ''
        for ic in range(1, N+1):
            exam1 += t1[N-ic][i-1]
            exam2 += t1[N-i][N-ic]
            exam3 += t1[ic-1][N-i]
        print(exam1, exam2, exam3)