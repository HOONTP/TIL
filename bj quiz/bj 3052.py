B = set([])
for i in range(10):
    A = int(input())
    B.add(A % 42)
print(len(B))