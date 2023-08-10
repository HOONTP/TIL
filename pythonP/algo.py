import sys
input = sys.stdin.readline

def fib(n):
    global cnt
    if n == 1 or n == 2:
        cnt += 1
        return 1 # 코드1
    else:
        return fib(n - 1) + fib(n - 2)

def fibon(n):
    global count
    f[1] = f[2] = 1
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
        count += 1
    return f[n]

N = int(input())

f = [0]*(N+1)
cnt = 0
count = 0
fib(N)
fibon(N)

print(cnt, count)