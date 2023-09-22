import sys
input = sys.stdin.readline

def sepa(s, e, n):
    one = '1'*n
    zero = '0'*n
    for i in range(n):
        if arr[s+i][e:e+n] != one:
            break
    else:
        return '1'
    for i in range(n):
        if arr[s+i][e:e+n] != zero:
            break
    else:
        return '0'

    S = s + n // 2
    E = e + n // 2
    m = n // 2
    return '(' + sepa(s, e, m) + sepa(s, E, m) + sepa(S, e, m) + sepa(S, E, m) + ')'


    pass
N = int(input())

arr = [input() for _ in range(N)]

result = sepa(0, 0, N)
print(result)