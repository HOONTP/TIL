import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
a, b = map(int, input().split())
c, d = map(int, input().split())

A = a*d + b*c
B = b * d

A_ = int(A / gcd(A, B))
B_ = int(B / gcd(A, B))
print(A_, B_)