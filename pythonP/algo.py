import sys
input = sys.stdin.readline

def binary_search(s):
    global K
    start = s
    end = N * N

    while start <= end:

        mid = (start + end) // 2  # 중간 인덱스 계산

        cnt = 0
        for i in range(1, N+1):
            S = i
            E = i*N
            if E <= mid:
                cnt += N
                continue
            while S <= E:
                M = (S+E) // 2
                if M == mid:
                    cnt += M // i
                    break
                elif M > mid:
                    E = mid - 1
                else:
                    S = mid + 1
            if M != mid:
                cnt += mid // i
        if cnt == K:
            return mid
        elif cnt > K:
            end = mid - 1
        else:
            start = mid + 1
    if cnt < K:
        return binary_search(s+1)
    else:
        return mid


N = int(input())
K = int(input())

result = binary_search(1)
print(result)