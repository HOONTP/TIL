import sys
input = sys.stdin.readline

def ML(n):
    print(n, end='')
    if LD[n] != '.':
        ML(LD[n])
    if RD[n] != '.':
        ML(RD[n])

def LM(n):
    if LD[n] != '.':
        LM(LD[n])
    print(n, end='')
    if RD[n] != '.':
        LM(RD[n])

def LRM(n):
    if LD[n] != '.':
        LRM(LD[n])
    if RD[n] != '.':
        LRM(RD[n])
    print(n, end='')

N = int(input())
LD = {}
RD = {}
for _ in range(N):
    M, L, R = input().split()
    LD[M] = L
    RD[M] = R

ML('A')
print()
LM('A')
print()
LRM('A')
print()