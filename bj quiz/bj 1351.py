import sys
input = sys.stdin.readline

N, P, Q = list(map(int, input().split()))

A = [1]

for i in range(1,N+1):
    ip = int(i/P)
    iq = int(i/Q)
    
    A.append(A[ip] + A[iq])

print(A[N])