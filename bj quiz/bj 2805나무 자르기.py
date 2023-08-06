import sys
input = sys.stdin.readline
# sys.stdin = open('input.in')

N, M = map(int, input().split())

lst = list(map(int, input().split()))

end_p = max(lst)
sta_p = 0
result = 0

while sta_p <= end_p:# 마지막 탈출 지점이 항상 여기인 것을 생각할 것.
    sum_d = 0
    mid = (sta_p + end_p) // 2 #변수 초기화 위치를 잘 골라야 할듯 if문 마다 쓰면 안되고.
    for i in lst:
        if i > mid:
            sum_d += i - mid
        if sum_d > M: #넘을 경우 일찍 탈출 시키기 / 처음에 여기서 실수가 발생한듯
            break
    if sum_d < M:
        end_p = mid - 1
    else:
        sta_p = mid + 1
        result = mid #최대한 덜 잘렸을 때가 정답. 넘더라도 다음 넘는 지점 전까지는 얘가 정답.

print(result)

###
# mid = (sum(lst)-M)//N
# lst.sort()
# end_p = lst[-1]
# sta_p = lst[0]
#
# while sta_p < end_p:
#     sum_d = 0
#     for i in lst:
#         if i - mid > 0:
#             sum_d += i - mid
#         if sum_d > M:
#             sta_p = mid + 1
#             result = mid
#             mid = (sta_p + end_p) // 2
#             sums = sum_d
#             break
#     if sum_d < M:
#         end_p = mid - 1
#         result = mid
#         mid = (sta_p + end_p) // 2
#         sums = sum_d
#     elif sum_d == M:
#         sums = sum_d
#         result = mid
#         break
# if sums < M:
#     print(mid+1)
# else:
#     print(mid)