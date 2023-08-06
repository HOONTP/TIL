import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
a, b = map(int, input().split())

result = (a*b)//gcd(a,b)

print(result)