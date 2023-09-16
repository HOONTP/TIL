import sys
input = sys.stdin.readline
import heapq

def prq(n):
    if n > 0:
        heapq.heappush(q, n+0.1)
    else:
        heapq.heappush(q, -(n+0.1))

def prt():
    a = heapq.heappop(q)
    if a % 1 > 0.5:
        return -round(a)
    else:
        return round(a)

N = int(input())
q = []
for _ in range(N):
    inp = int(input())
    if inp:
        prq(inp)
    else:
        if q:
            print(prt())
        else:
            print(0)
