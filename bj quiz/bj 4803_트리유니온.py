import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def find(x):
    if dic_[x] == x:
        return x
    dic_[x] = find(dic_[x])
    return dic_[x]

def unionset(a, b):
    A = find(a)
    B = find(b)

    if A == B:
        dic_[A] = 0
    elif A == 0:
        dic_[B] = 0
    elif B == 0:
        dic_[A] = 0
    else:
        dic_[A] = B

tc = 0
while True:
    N, E = map(int, input().split())
    tc += 1
    if N == 0 and E == 0:
        break

    dic_ = list(range(N+1))

    for _ in range(E):
        a, b = map(int, input().split())
        unionset(a, b)

    for i in range(1, N+1):
        find(i)
    result = set(dic_)
    ans = len(result) - 1
    if ans == 0:
        print(f"Case {tc}: No trees.")
    elif ans == 1:
        print(f"Case {tc}: There is one tree.")
    else:
        print(f"Case {tc}: A forest of {ans} trees.")