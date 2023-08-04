import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    result = 0
    while True:
        i = 2
        while i < N+1:
            if i == N:
                result = N
                break
            if N % i == 0:
                break
            i += 1
        if result == N:
            break
        N += 1

    print(result)