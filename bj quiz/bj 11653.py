import sys
input = sys.stdin.readline

N = int(input())

i = 2
lst = []
while N != 1:
    while N % i == 0:
        N = N / i
        lst.append(i) 
    i += 1

for _ in lst:
    print(_)