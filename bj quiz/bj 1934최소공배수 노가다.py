import sys
input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1):
    A, B = map(int, input().split())
    result = 0
    num_A = A #작은 수
    if B % A == 0:
        result = B
    else:
        num = 2
        while A > num:
            while A % num == 0 and B % num == 0:
                A = A/num
                B = B/num
            num += 1
        result = num_A * B #B=큰 수에서 공약수가 다 빠진 남은 수
    print(int(result))

### 유클리드 최대공약수 외우기
"""
def gcd(a, b): # a가 큰 수
    while b:
        a, b = b, a % b
    return a # 최대 공약수

result = (a * b) // gcd(a, b) # 두 수의 곱 // 최대 공약수
"""