import sys
input = sys.stdin.readline

N = int(input())
i = 1
while N > i:
    N -= i
    i += 1
if i % 2 == 0:
    print(f'{N}/{i+1-N}')
else:
    print(f'{i+1-N}/{N}')

#20 - 1 -2-3-4-5 < N=5, i=6
#N = 5 / 6=> 1/6 2/5 3/4 4/3 5/2 6/1 