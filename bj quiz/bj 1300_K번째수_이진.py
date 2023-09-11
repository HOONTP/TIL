import sys
input = sys.stdin.readline

def binary_search():
    start = 1
    end = N * N

    while start <= end:
        mid = (start + end) // 2  # 중간 인덱스 계산
        cnt = 0
        for i in range(1, N+1):
            if mid < i*N:
                cnt += mid // i
            else:
                cnt += N
        if cnt >= K:
            end = mid - 1
        else:
            start = mid + 1

    return start


N = int(input())
K = int(input())

result = binary_search()
print(result)