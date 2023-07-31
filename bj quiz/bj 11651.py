import sys
input = sys.stdin.readline
N = int(input())

lst = []
for _ in range(N):
    x, y = map(int, input().split())
    lst.append((x,y))

lst.sort(key = lambda x : (x[1], x[0]))

for it in lst:
    print(it[0], it[1])