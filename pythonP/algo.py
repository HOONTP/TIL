import sys
input = sys.stdin.readline
import heapq

sums = []
for _ in range(5):
    sums.append(int(input()))
sums.sort()
print(sum(sums)//5)
print(sums[2])