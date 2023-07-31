import sys
input = sys.stdin.readline
N = int(input())

import time
start_time = time.time()

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    V = list(map(int, input().split()))
    i = 0
    lst = []
    for i in range(N-M+1):
        sm = 0
        it = 0
        while it < M:
            sm += V[i+it]
        lst.append(sm)
    lst.sort()
    print(f'#{T} {lst[-1]-lst[0]}')


end_time = time.time()
print("time:", end_time - start_time)
