import sys
input = sys.stdin.readline
# import pprint

N, C = map(int, input().split())

arr = [0]*(10)
lst = []
print(arr)
for _ in range(N):
    a = int(input())
    lst.append(a)

lst.sort()
print(lst)