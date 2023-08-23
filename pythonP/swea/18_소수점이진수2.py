T = int(input())

for t in range(1, T+1):
    N = float(input())

    i = 1
    result = ''
    while N != 0:
        if i == 13:
            break
        if N // (1/2)**i:
            N = N % (1/2)**i
            result = result + '1'
        else:
            result = result + '0'
        i += 1

    if N != 0:
        print(f'#{t}', 'overflow')
    else:
        print(f'#{t}', result)