T = int(input())

for tc in range(1, T+1):
    N = input()
    result = ''
    for i in N:
        if i == 'b':
            result = 'd' + result
        elif i == 'd':
            result = 'b' + result
        elif i == 'p':
            result = 'q' + result
        else:
            result = 'p' + result

    print(f'#{tc}', result)