N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort()
totalSum = 0
for i in range(N):
    totalSum += A[i] * B[i]
print(totalSum)