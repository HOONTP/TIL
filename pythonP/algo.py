import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**9)

A, B, C = map(int, input().split())

if B >= C:
    print(-1)
else:
    result = (A // (C - B)) + 1
    print(result)