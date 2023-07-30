import sys
import time
input = sys.stdin.readline
start_time = time.time()
# N = int(input())

last_char = '3'
if '20' <= last_char <= '10':
    print(True)
else:
    print(False)

end_time = time.time()
print("time:", end_time - start_time)
