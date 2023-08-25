T = int(input())
'''
2는 가능하면 무조건 주기
1은 홀수 위주로 담되 2가 하나만 있다면 쉬기.
'''
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    lst.sort()
    mx = lst[-1]
    cnt = 0

    while lst and lst[-1] == mx:
        lst.pop()

    while lst:
        if lst[-1] == mx:
            lst.pop()

        if lst:
            for i in range(len(lst)-1, -1, -1):
                if (mx-lst[i]) % 2 == 1:
                    lst[i] += 1
                    break
            else:
                if len(lst) == 1 and mx - lst[-1] == 2:
                    pass
                else:
                    lst[-1] += 1
            cnt += 1
        else:
            break

        lst.sort()

        if lst[-1] == mx:
            lst.pop()

        if lst:
            for i in range(len(lst)):
                if (mx-lst[i]) != 1:
                    lst[i] += 2
                    break
            cnt += 1
        else:
            break

        lst.sort()
    print(f'#{tc}', cnt)