import sys
input = sys.stdin.readline
'''
i j  m = n // 3
i+m j
i+2m j
i j+m
i j+2m
i+m j+m
for i in range(3):
    for j in range(3):
        delete(m, i*m, j*m)
'''

def delete(n, a, b):
    m = n//3
    for i in range(m):
        for j in range(m):
            lst[a+m+i][b+m+j] = ' '

    if n <= 3:
        return

    for k in range(3):
        for l in range(3):
            if k != 1 or l != 1:
                delete(m, a+k * m, b+l * m)


N = int(input())
lst = [['*']*N for _ in range(N)]# N은 3의 제곱이다 라는 말 보고 N**3함 레전드

delete(N, 0, 0)

for i in lst:
    print(''.join(i))#이거 *i 했다가 계속 틀림
