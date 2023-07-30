import sys
input = sys.stdin.readline

N = int(input()) -1
i = 6
count = 1
while N > i:
    N -= i
    i += 6
    count += 1

if N == 0:
    print(count)
else:
    print(count+1)