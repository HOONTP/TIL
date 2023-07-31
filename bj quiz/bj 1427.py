import sys
input = sys.stdin.readline
N = input()
print(*sorted(N, reverse=True), sep="")