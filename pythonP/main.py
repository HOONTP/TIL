def uni_find(x):
    if dic_[x] != x:
        dic_[x] = uni_find(dic_[x])
    return dic_[x]

def uni_set(a, b, w):
    A = uni_find(a)
    B = uni_find(b)
    if A != B:
        if point[A] < point[B]:
            mid = sums[a] - sums[b] + w
            for i in [key for key, value in dic_.items() if value == A]:
                sums[i] -= mid
            dic_[A] = B
            cal = point[A] + point[B]
            point[A] = cal
            point[B] = cal
        else:
            mid = sums[a] - sums[b] + w
            for i in [key for key, value in dic_.items() if value == B]:
                sums[i] += mid
            dic_[B] = A
            cal = point[A] + point[B]
            point[A] = cal
            point[B] = cal
    else:
        sums[b] = sums[a] + w


for t in range(1, int(input())+1):
    V, M = map(int, input().split())
    lst = [[] for _ in range(V+1)]
    sb = []
    dic_ = {i:i for i in range(V+1)}
    sums = [0] * (V + 1)
    point = [1] * (V+1)

    for _ in range(M):
        W = input().split()
        if W[0] == '!':
            s, e, v = map(int, W[1:])
            uni_set(s, e, v)
            # print(sums)
            # print(dic_)
            # print(point)
        else:
            s, e = map(int, W[1:])
            S = uni_find(s)
            E = uni_find(e)
            if S == E:
                result = sums[e] - sums[S] - sums[s]
                sb.append(result)
            else:
                sb.append("UNKNOWN")

    print(f'#{t}', *sb)