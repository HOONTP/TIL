import sys
input = sys.stdin.readline
import heapq

def prq(n):
    heapq.heappush(q, n)



N = int(input())
q = []
for _ in range(N):
    inp = int(input())
    if inp:
        prq(inp)
    else:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)