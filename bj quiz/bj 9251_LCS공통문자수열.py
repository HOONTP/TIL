import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()

N_A = len(A)
N_B = len(B)
result = [0] * (N_B+1)
for i in range(N_A):
    for j in range(N_B-1, -1, -1):
        if A[i] == B[j]:
            result[j+1] = max(result[:j+1]) + 1

print(max(result))