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

