def backT(lst, cnt):
    global mx
    if cnt == M:
        sums = ''
        for num in lst:
            sums = sums + str(num)
        sums = int(sums)
        if mx < sums:
            mx = sums
        return

    if cnt < N-1:
        high = 0
        count = cnt
        while True:
            if count == N-1: # 3
                lst[-1], lst[-2] = lst[-2], lst[-1]
                break
            for i in range(N-1, count - 1, -1):
                if lst[i] >= high:
                    high = lst[i]
                    ind = i
            if ind == count:
                high = 0
                count += 1
            else:
                lst[count], lst[ind] = lst[ind], lst[count]
                break
        backT(lst, cnt+1)
    else:
        lst[-1], lst[-2] = lst[-2], lst[-1]
        backT(lst, cnt+1)

def backS(lst, cnt):
    global mx
    if cnt == M:
        sums = ''
        for num in lst:
            sums = sums + str(num)
        sums = int(sums)
        if mx < sums:
            mx = sums
        return
    for w in range(N):
        for target in range(w+1 ,N):
            if w != target:
                lst[w], lst[target] = lst[target], lst[w]
                backS(lst, cnt + 1)
                lst[w], lst[target] = lst[target], lst[w]

T = int(input())

for tc in range(1, T+1):
    nums, M = input().split()

    N = len(nums)
    M = int(M)

    lst = []
    for i in nums:
        lst.append(int(i))

    result = []
    mx = 0
    if nums == '0'*N:
        mx = nums
    elif N < M:
        backT(lst, 0)
    else:
        backS(lst, 0)

    print(f'#{tc}', mx)
    # else:
    #     arr = sorted(lst, reverse=True)# 이거 안된다.
    #     mx = int(''.join(arr))