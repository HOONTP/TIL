import sys
# sys.stdin = open('input.in')
input = sys.stdin.readline


N = int(input())
k = int(input())

lst = [i*j for i in range(1,N+1) for j in range(1, N+1)]

print(lst)

lst.sort()

print(lst[k])
