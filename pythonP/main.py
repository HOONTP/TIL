def uni_find(x):
    if dic_[x] != x:
        dic_[x] = uni_find(dic_[x])
    return dic_[x]

def uni_set(a, b, w):
    A = uni_find(a)
    B = uni_find(b)
    if A != B:
        mid = sums[b] - sums[a] - w
        for i in [key for key, value in dic_.items() if value == B]:
            # if uni_find(i) == B:
            sums[i] -= mid
        dic_[B] = A
    else:
        sums[b] = sums[a] + w

for t in range(1, int(input())+1):
    V, M = map(int, input().split())
    lst = [[] for _ in range(V+1)]
    sb = []
    dic_ = {i:i for i in range(V+1)}
    sums = [0] * (V + 1)

    for _ in range(M):
        W = input().split()
        if W[0] == '!':
            s, e, v = map(int, W[1:])
            uni_set(s, e, v)
            # lst[s].append((e, v))
            # lst[e].append((s, -v))
        else:
            s, e = map(int, W[1:])
            S = uni_find(s)
            E = uni_find(e)
            if S == E:
                result = sums[e] - sums[S] - sums[s]
                sb.append(result)
            else:
                sb.append("UNKNOWN")
        print(sums)
        print(dic_)
    print(f'#{t}', *sb)