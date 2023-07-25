N, M = map(int, input().split())
A = []
for i in range(1, N+1):
    A.append(i)

for ic in range(M):
    a, b = map(int, input().split())
    B = (1 + b - a) // 2
    if B == 0:
        continue
    else:
        for it in range(B):
            A[-1 + a + it], A[-1 + b - it] = A[-1 + b - it], A[-1 + a +it]
for id in range(N):
    print(A[id], end = ' ')