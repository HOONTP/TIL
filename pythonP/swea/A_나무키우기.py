T = int(input())


for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    mx = max(lst)
    cnt = 0
    if mx == 1:#ㅇㅣ게 극혐인거네
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

    if A > B:
        cnt += A*2 - 1
    else:
        cnt += B*2
    print(f'#{tc}', cnt)

#백트리트?

'''
back인건 좋아 그래
그러면 물을 주는 기준을 어떻게 할거냐?
누구를 우선적으로 줄거냐 모든 케이스를 다 주기에는 너무 복잡도 올라간다.
N = 100 / 차이가 1 에서 120까지니까, 1만번째 시행에 나올 수도 있는데 그걸 100만 번 괜찮나?

일단 가장 합리적인 것은 max 값을 키울 이유는 없다. 그러면 내가 줄 때 max값보다 커지면 안준다.
'''
"""
def backT(arr, cnt, day, rest):
    # print(arr,day)
    global count
    count += 1
    print(arr, cnt, result[-1])
    if cnt > result[-1]:
        return
    if min(arr) == mx:
        result.append(cnt)
        return
    if day == 1: # pwr = 1
        if rest == 0:
            backT(arr, cnt + 1, 2, 1)

        pwr = 1
        for i in range(N):
            if arr[i] + pwr <= mx:
                arr[i] += pwr
                backT(arr, cnt + 1, 2, 0)
                arr[i] -= pwr
                break

    elif day == 2: # pwr = 2
        if rest == 0:
            backT(arr, cnt + 1, 1, 1)

        pwr = 2
        for i in range(N):
            if arr[i] + pwr <= mx:
                arr[i] += pwr
                backT(arr, cnt + 1, 1, 0)
                arr[i] -= pwr
                break
열 받지만 백트래킹으로 안되는 것 같기도?
# backT(lst, 0, 1, 0)

"""