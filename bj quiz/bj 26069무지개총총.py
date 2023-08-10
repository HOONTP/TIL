import sys
input = sys.stdin.readline

N = int(input())
dance = {'ChongChong'}

for i in range(N):
    A, B = input().split()

    if A in dance:
        dance.add(B)
    elif B in dance:
        dance.add(A)

print(len(dance))