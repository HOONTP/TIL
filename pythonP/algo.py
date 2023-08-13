import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()

N_B = len(B)
result = [0] * (N_B+1)

if A == B:
    print(N_B)
elif B in A:
    print(N_B)
elif A in B:
    print(len(A))
else:
    for i in A:
        # print(result)
        for j in range(N_B-1, -1, -1):
            if i == B[j]:
                result[j+1] = max(result[:j+1]) + 1

    print(max(result))