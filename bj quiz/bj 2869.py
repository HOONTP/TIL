import sys
input = sys.stdin.readline


A, B, V = list(map(int, input().split()))

T = A - B

result1 = (V-A) // T
result2 = (V-A) % T

if result2 == 0:
    print( result1 + 1 )
else:
    print( result1 + 2 )