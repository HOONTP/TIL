dic_ = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111',
        '0111011', '0110111', '0001011']

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = [input() for _ in range(N)]
    check = ['0' for _ in range(M)]
    check = ''.join(check)
    for i in A:
        if i != check:
            A = i
            break
    result = []
    i = M
    F = 0

    while i > 0:
        n = A[i-6:i+1]
        if n in dic_:
            while i < M:
                a = A[i-6:i+1]
                for k in dic_:
                    if k == a:
                        result.append(dic_.index(k))
                        i -= 7
                        break
                else:
                    F = -1
                    break
        if F == -1:
            break
        i -= 1
    sums = 0
    for i in range(len(result)//2-1, -1, -1):
        sums += result[i*2+1]*3
        sums += result[i*2]

    if sums % 10 == 0:
        print(f'#{tc}', sum(result))
    else:
        print(f'#{tc}', 0)