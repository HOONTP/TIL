def counting(S, arr):
    i, j = S[0], S[1]
    for k in range(1, L):
        if j + k + 1 < N:
            if arr[i][j + k] == arr[i][j + k + 1]:
                pass
            else:
                return 0
        else:
            return 0
    if j + L + 1 < N and arr[i][j+L] < arr[i][j+L+1]:
        return 0
    return 1

def counting_minus(S, arr):
    i, j = S[0], S[1]
    for k in range(1, L):
        if 0 <= j - k - 1:
            if arr[i][j - k] == arr[i][j - k - 1]:
                pass
            else:
                return 0
        else:
            return 0
    if 0 <= j - L - 1 and arr[i][j-L] < arr[i][j-L-1]:
        return 0
    return 1

# 가운데 L보다 큰 홈이 생긴 경우를 고려하기 위해서 arr을 통쨰로 받는 def를 짜야할 것 같음,,,
N, L = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
lst = list(zip(*arr))
print(arr)
print(lst)
result = set()
for i in range(N):
    j = 0
    while 0 <= j < N:
        if j == N-1:
            print(i)
            result.add((i, 1))
            break
        if arr[i][j] - arr[i][j+1] == 1:
            mid = counting((i, j), arr)
            if mid == True:
                j += L -1
            else:
                break
        elif lst[i][j+1] - lst[i][j] == 1:
            mid = counting_minus((i, j+1), lst)
            if mid != True:
                break
        elif abs(arr[i][j] - arr[i][j+1]) > 1:
            break
        j += 1

# for i in range(N):
#     j = N-1
#     while 0 <= j < N:
#         if j == 0:
#             print(i)
#             result.add((i, 1))
#             break
#         if arr[i][j] - arr[i][j-1] == 1:
#             mid = counting_minus((i, j), arr)
#             if mid == True:
#                 j -= L -1
#             else:
#                 break
#
#         elif abs(arr[i][j] - arr[i][j-1]) > 0:
#             break
#         j -= 1

for i in range(N):
    j = 0
    while 0 <= j < N:
        if j == N-1:
            result.add((i, 2))
            print(i, 'b')
            break
        if lst[i][j] - lst[i][j+1] == 1:
            mid = counting((i, j), lst)
            if mid == True:
                j += L -1
            else:
                break
        elif lst[i][j+1] - lst[i][j] == 1:
            mid = counting_minus((i, j+1), lst)
            if mid != True:
                break
        elif abs(lst[i][j] - lst[i][j+1]) > 1:
            break
        j += 1


# for i in range(N):
#     j = N-1
#     while 0 <= j < N:
#         if j == 0:
#             result.add((i, 2))
#             print(i, 'b')
#             break
#         if lst[i][j] - lst[i][j-1] == 1:
#             mid = counting_minus((i, j), lst)
#             if mid == True:
#                 j -= L -1
#             else:
#                 break
#         elif abs(lst[i][j] - lst[i][j-1]) > 0:
#             break
#         j -= 1
print(sorted(result, key=lambda x:x[1]))
