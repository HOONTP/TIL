import sys
input = sys.stdin.readline

N = int(input())

stack = []
size = 0
sums = 0

for _ in range(N):
    x, r = map(int, input().split())
    sums += 1
    if size == 2:
        if stack[0] == x-r and stack[-1] == x+r:
            sums += 1