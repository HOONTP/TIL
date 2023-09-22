def uni_find(x):
    if dic_[x] != x:
        dic_[x] = uni_find(dic_[x])
    return dic_[x]

def uni_set(a, b):
    A = uni_find(a)
    B = uni_find(b)
    if A < B:
        dic_[B] = A
    elif A > B:
        dic_[A] = B

def prim(start, end):
    sums = [0] * (V + 1)
    visited = [False] * (V + 1)
    q = []
    q.append(start)

    while q:
        n = q.pop()
        visited[n] = True
        if lst[n]:
            for i, w in lst[n]:
                if i == end:
                    sums[i] = sums[n] + w
                    lst[start].append((i, sums[i]))
                    return sums[end]
            for i, w in lst[n]:
                if visited[i] == False:
                    sums[i] = sums[n] + w
                    q.append(i)
                    lst[start].append((i, sums[i]))
                    break

for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    lst = [[] for _ in range(V+1)]
    sb = []
    dic_ = list(range(V+1))

    for _ in range(E):
        W = input().split()
        if W[0] == '!':
            s, e, v = map(int, W[1:])
            uni_set(s, e)
            lst[s].append((e, v))
            lst[e].append((s, -v))
        else:
            s, e = map(int, W[1:])
            if uni_find(s) == uni_find(e):
                result = prim(s, e)
                sb.append(result)
            else:
                sb.append("UNKNOWN")
    print(f'#{t}', *sb)