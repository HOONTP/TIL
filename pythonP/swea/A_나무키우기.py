# T = int(input())

# def backT(arr, cnt, day):
#     # print(arr, cnt,'cnt', day, result)
#     if min(arr) == mx:
#         result.append(cnt)
#         return
#     if result:
#         if cnt >= min(result):
#             return
# # 선행된 함수의 결과가 그 아래에서 호출된 함수에 영향을 미칠 수 있으므로, 하나의 함수 내에서는 한 조건에 하나의 트래킹만 보내야 한다.
#     if day == 1: # pwr = 1
#         for i in range(N):
#             if mx - arr[i] == 1:
#                 arr[i] += 1
#                 backT(arr, cnt + 1, 2)
#                 return
#         else:#min != max 모든 수가 2차이 인 경우
#             if arr.count(mx-2) == 1:
#                 backT(arr, cnt + 1, 2)
#                 return
#             else:
#                 for i in range(N):
#                     if arr[i] != mx:
#                         arr[i] += 1
#                         backT(arr, cnt + 1, 2)
#                         return
#
#     elif day == 2: # pwr = 2
#         for i in range(N):
#             if mx - arr[i] == 2:
#                 arr[i] += 2
#                 backT(arr, cnt + 1, 1)
#                 return
#         else:# 맥스가 아닌 모든 수가 1차이
#             backT(arr, cnt + 1, 1)
#             return
#     return
#
#
# for tc in range(1, T+1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     mx = max(lst)
#     count = 0
#     for i in range(N):
#         n = 0
#         if lst[i] < mx:
#             n = ((mx - lst[i]) // 3)
#             count += n*2
#             lst[i] = lst[i] + n*3
#     lst.sort(reverse=True)
#     result = []
#     backT(lst, count, 1)
#
#     print(f'#{tc}', min(result))



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    mx = max(lst)
    cnt = 0
    if mx == 1:
        print(f'#{tc}', cnt)
        continue
    elif mx == 2:
        print(f'#{tc}', lst.count(1)*2 -1)
        continue

    for i in range(N):
        if lst[i] < mx:
            cnt += ((mx - lst[i]) // 3)*2
        lst[i] = (mx - lst[i]) % 3
    A = lst.count(1)
    B = lst.count(2)
    # print(lst)
    # print(A, B, cnt)

    if A > B:
        cnt += A*2 - 1
    else:
        cnt += A*2
        B = B - A
        cnt += (B//3) * 4
        B = B % 3
        cnt += (B//2) * 3
        B = B % 2
        if B == 2:
            cnt += 1
        elif B == 1:
            cnt += 2

    print(f'#{tc}', cnt)

#백트리트?

'''
back인건 좋아 그래
그러면 물을 주는 기준을 어떻게 할거냐?
누구를 우선적으로 줄거냐 모든 케이스를 다 주기에는 너무 복잡도 올라간다.
N = 100 / 차이가 1 에서 120까지니까, 1만번째 시행에 나올 수도 있는데 그걸 100만 번 괜찮나?

일단 가장 합리적인 것은 max 값을 키울 이유는 없다. 그러면 내가 줄 때 max값보다 커지면 안준다.
'''

# T = int(input())
#
# def backT(arr, cnt, day):
#     # print(arr, cnt, day)
#     if min(arr) == mx:
#         result.append(cnt)
#         return
#     if result:
#         if cnt >= min(result):
#             return
#
#     if day == 1: # pwr = 1
#         for i in range(N):
#             if mx - arr[i] != 2 and arr[i] != mx:
#                 arr[i] += 1
#                 backT(arr, cnt + 1, 2)
#                 arr[i] -= 1
#                 break
#         else:#min != max 모든 수가 2차이 인 경우
#             for i in range(N):
#                 if arr[i] != mx:
#                     backT(arr, cnt + 1, 2)
#                     arr[i] += 1
#                     backT(arr, cnt + 1, 2)
#                     arr[i] -= 1
#                     break
#
#     elif day == 2: # pwr = 2
#         for i in range(N):
#             if mx - arr[i] != 1 and arr[i] != mx:  # 맥스 아니고 1차이 아니면
#                 arr[i] += 2
#                 backT(arr, cnt + 1, 1)
#                 arr[i] -= 2
#                 break
#         else:# 맥스가 아닌 모든 수가 1차이
#             backT(arr, cnt + 1, 1)
#
#
# for tc in range(1, T+1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     mx = max(lst)
#     count = 0
#     for i in range(N):
#         n = 0
#         if lst[i] < mx:
#             n = ((mx - lst[i]) // 3)
#             count += n*2
#             lst[i] = lst[i] + n*3
#     lst.sort(reverse=True)
#     result = []
#     backT(lst, count, 1)
#
#     print(f'#{tc}', min(result))