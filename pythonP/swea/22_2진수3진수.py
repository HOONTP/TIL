def out(lst, n):
    st = ''
    if n == 2:
        for i in lst:
            st = st + str(i)
        return int(st, 2)
    elif n == 3:
        for i in lst:
            st = st + str(i)
        return int(st, 3)
T = int(input())

for tc in range(1, T+1):
    binary = list(map(int, input()))
    ternary = list(map(int, input()))

    for i in range(len(binary)):
        if binary[i] == 1:
            binary[i] = 0
        else:
            binary[i] = 1
        for j in range(len(ternary)):
            n = ternary[j]
            for k in range(3):
                if n != k:
                    ternary[j] = k
                    if out(binary, 2) == out(ternary, 3):
                        print(f'#{tc}', out(binary, 2))
            ternary[j] = n
        if binary[i] == 1:
            binary[i] = 0
        else:
            binary[i] = 1