T = int(input())

def check(arr):
    arr.sort()
    arr_set = set(arr)
    arr_set = sorted(arr_set) # 1 2 2 3 의 경우 연속인지 확인이 어렵다 그래서 set으로 중복 제거
    for i in range(len(arr)-2):
        if arr[i] == arr[i+1] and arr[i+1] == arr[i+2]:
            return True
    for i in range(len(arr_set)-2):
        if arr_set[i]+2 == arr_set[i+1]+1 == arr_set[i+2]:
            return True
    else:
        return False


for tc in range(1, T+1):
    lst = list(map(int, input().split()))

    A_card = []
    B_card = []

    for i in range(12):
        if i % 2 == 0:
            A_card.append(lst[i])
            if check(A_card):
                print(f'#{tc}', 1)
                break
        else:
            B_card.append(lst[i])
            if check(B_card):
                print(f'#{tc}', 2)
                break
    else:
        print(f'#{tc}', 0)