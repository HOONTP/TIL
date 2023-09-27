import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def find(x):
    if x == dic_[x]:
        return x
    dic_[x] = find(dic_[x])
    return dic_[x]

def uniset(a, b):
    A = find(a)
    B = find(b)
    if A != B:
        dic_[A] = B
        return 0
    else:
        return 1

def prt():
    for _ in range(M):
        a, b = map(int, input().split())
        same = uniset(a, b)
        # 두개의 부모가 같은 순간 사이클이 형성된다.
        if same:
            return _+1
    return 0

N, M = map(int, input().split())
dic_ = list(range(N))

result = prt()
print(result)