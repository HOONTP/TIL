import sys
input = sys.stdin.readline

def triple(a, b, c):
    global dic_

    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        return triple(20, 20, 20)

    elif (a, b, c) in dic_:
        return dic_[(a, b, c)]

    elif a < b and b < c and (a, b, c) not in dic_:
        dic_[(a, b, c)] = triple(a, b, c - 1) + triple(a, b - 1, c - 1) - triple(a, b - 1, c)
        return dic_[(a, b, c)]

    else:
        dic_[(a, b, c)] = triple(a - 1, b, c) + triple(a - 1, b - 1, c) + triple(a - 1, b, c - 1) - triple(a - 1, b - 1, c - 1)
    return dic_[(a, b, c)]

while True:
    a, b, c = map(int, input().split())
    dic_ = {}
    if a == b == c == -1:
        break
    A = (a, b, c)
    print(f'w{A} =', triple(a, b, c))
