import sys
input = sys.stdin.readline
# N = int(input())

import time
start_time = time.time()

print(min(5, 10) > max(1, 100))
end_time = time.time()
print("time:", end_time - start_time)
