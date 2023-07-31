import sys
import time
input = sys.stdin.readline
N = int(input())

mod_ = N//3
result = 0
for i in range(mod_+1):
    if (N - 3*i) % 5 == 0:
        result = (N-3*i)//5 + i
        print(result)
        quit()
print(-1)