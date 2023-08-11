import sys
input = sys.stdin.readline

def rgb(N):
    dic_[0, 0] = arr[0][0]
    dic_[0, 1] = arr[0][1]
    dic_[0, 2] = arr[0][2]
    for n in range(1, N):
        dic_[n, 0] = min(dic_[n - 1, 1] + arr[n][0], dic_[n - 1, 2] + arr[n][0])
        dic_[n, 1] = min(dic_[n - 1, 0] + arr[n][1], dic_[n - 1, 2] + arr[n][1])
        dic_[n, 2] = min(dic_[n - 1, 0] + arr[n][2], dic_[n - 1, 1] + arr[n][2])

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dic_ = {}
rgb(N)
print(min(dic_[N-1, 1], dic_[N-1, 2],dic_[N-1, 0]))

# n번째 직전인 n-1까지의 3가지 경우의 최솟 값 각각 구하기 + 지금 3자리와 교차한 모든 최소 값 구하기
# 3 * 2 회 각각 2경우의 수 중 최소값 하나 계산