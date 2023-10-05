import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    x, r = map(int, input().split())
    lst.append((x, r))
print(lst)
lst.sort(key = lambda x:x[1])
print(lst)

X, R = lst.pop()

