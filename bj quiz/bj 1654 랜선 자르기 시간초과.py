import sys
# sys.stdin = open('input.in')
input = sys.stdin.readline

K, N = map(int, input().split())

lst = [int(input()) for _ in range(K)]

end = max(lst)
start = 0

while start <= end:
    cnt = 0
    mid = (end + start) // 2

    for i in lst:
        if mid > 0:
            cnt += i // mid
        if cnt > N:
            break
    if cnt < N:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
    if mid == 0: # 0, 1이 되어서 분모가 0이되는 순간 고려.
        result = 1
        start = mid + 1

print(result)

# sum_ = sum(lst)
# aver = sum_//N
#
# while True:
#     cnt = 0
#
#     for i in lst:
#         cnt += i // aver
#
#     if cnt >= N:
#         break
#     aver -= 1 # 이부분을 이진탐색으로 변환해야하는 거지
# print(aver)