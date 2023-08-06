import sys
# sys.stdin = open('input.in')
input = sys.stdin.readline

def fac(N):
    if N == 1 or N == 0:
        return 1
    return N * fac(N-1)

T = int(input())

for _ in range(T):# for문으로 M/i M-=1 하니깐 틀렸다고 나옴.(실수형의 미세차이 때문인듯) round 쓰면 맞았다 하려나? round는 맞다고 하네. 오차를 없애고 싶으면 round
    N, M = map(int, input().split())

    result = int(fac(M) / (fac(N) * fac(M-N)))

    print(result)

# def binomial_coefficient(n, k): nCr 조합
#     if k == 0 or k == n:
#         return 1
#     return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)
# 1번이 선택됐을 경우 + 1번이 선택 안됐을 경우

# def binomial_coefficient(n, k): 동적 계획법
#     dp = [[0] * (k+1) for _ in range(n+1)]
#
#     for i in range(n+1):
#         for j in range(min(i, k)+1):
#             if j == 0 or j == i:
#                 dp[i][j] = 1
#             else:
#                 dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
#
#     return dp[n][k]
