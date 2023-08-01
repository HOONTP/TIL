import sys
input = sys.stdin.readline
N = int(input())

import time
start_time = time.time()

N, T = map(int, input().split())

print(N, T)


end_time = time.time()
print("time:", end_time - start_time)
