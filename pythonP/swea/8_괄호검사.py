T = int(input())

for tc in range(1, T+1):
    N = input()

    wait_lst =['!']
    result = 1
    i = 0
    n = len(N)

    while i < n:
        if N[i] == '{' or N[i] == '(':
            wait_lst.append(N[i])

        elif N[i] == '}':
            if wait_lst[-1] == '{':
                wait_lst.pop()
            else:
                result = 0
                break

        elif N[i] == ')':
            if wait_lst[-1] == '(':
                wait_lst.pop()
            else:
                result = 0
                break
        i += 1
    if len(wait_lst) > 1:
        result = 0
    print(f'#{tc}', result)