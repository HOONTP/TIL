T = int(input())

for tc in range(1, T+1):
    N = list(input())

    wait_lst =['!']
    N.reverse()

    while N:
        if wait_lst[-1] == N[-1]:
            wait_lst.pop()
            N.pop()
        else:
            wait_lst.append(N.pop())

    result = len(wait_lst)-1
    print(f'#{tc}', result)