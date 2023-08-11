T = int(input())

for tc in range(1, T+1):
    arr = [['']*15 for _ in range(5)]

    for _ in range(5):
        sen = input()
        for i in range(len(sen)):
            arr[_][i] = sen[i]

    print(f'#{tc}', end=' ')
    for j in range(15):
        for i in range(5):
            print(arr[i][j], end='')
    print()

