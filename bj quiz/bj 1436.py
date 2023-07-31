import sys
import time
input = sys.stdin.readline
N = int(input())

lst = []
for i in range(3000000):
    if '666' in str(i):
        lst.append(i)

print(lst[N-1])