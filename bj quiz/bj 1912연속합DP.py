# 입력 받기
n = int(input())
numbers = list(map(int, input().split()))

# dp 배열 초기화
# dp[i]: i번째 수까지의 연속된 부분 수열 중 최대 합
dp = [0] * n

# 첫 번째 숫자로 초기화
dp[0] = numbers[0]

# 동적 계획법으로 최대 부분 합 구하기
for i in range(1, n):
    # i번째 수를 포함하는 부분 수열 중에서 최대 합을 선택
    # (이전까지의 최대 합 + 현재 숫자) 또는 현재 숫자 중에서 큰 값을 선택
    dp[i] = max(dp[i - 1] + numbers[i], numbers[i])# (dp[i-1], 를 추가하면 항상 최대값 아닌가?)

# dp 배열 중 최대 값을 찾아 반환
max_sum = max(dp)
print(max_sum)
(({ )