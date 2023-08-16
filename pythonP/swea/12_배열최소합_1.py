T = int(input())

def backt(A, now_A):
    if len(now_A) == N:
        sums = 0
        for i in range(N):
            sums += arr[i][now_A[i]]
        result.append(sums)
        return

    for a in A:
        if a not in now_A:
            now_A.append(a)
            backt(A, now_A)
            now_A.pop()

# def sup(A):
#     backt(A, [])
for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    sums = 0

    A = [i for i in range(N)]

    SUM = 0
    result = []

    backt(A, [])
    print(f'#{tc}', min(result))