
def uni_find(x):
    if dic_[x] != x:
        dic_[x] = uni_find(dic_[x])
    return dic_[x]

def uni_set(a, b):
    A = uni_find(a)
    B = uni_find(b)
    if A != B:
        dic_[B] = A
        # dic_[b] = A
    pass

for t in range(1, int(input())+1):
    N, M = map(int,input().split())
    dic_ = list(range(N+1))
    for _ in range(M):
        a, b = map(int, input().split())
        uni_set(a, b)
    set_ = set()
    cnt = 0
    for i in range(1, N+1):
        if uni_find(i) not in set_:
            set_.add(dic_[i])
            cnt += 1
    print(f'#{t}', cnt)