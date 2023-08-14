T = 10

for tc in range(1, T+1):
    N = int(input())
    nums = input()

    stack = []
    i = 0
    while i < N:
        if nums[i] == '+':
            stack.append(stack.pop()+int(nums[i+1]))
            i += 2
        else:
            stack.append(int(nums[i]))
            i += 1
    print(f'#{tc}', stack[0])