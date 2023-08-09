T = 10

for tc in range(1, T+1):
    N, nums = input().split()

    nums = list(nums)
    nums.reverse()
    wait_lst = ['!']

    while nums:
        if wait_lst[-1] == nums[-1]:
            wait_lst.pop()
            nums.pop()
        else:
            wait_lst.append(nums.pop())

    print(f'#{tc}', ''.join(wait_lst[1:]))
