T = int(input())

nums = [0] * 301#N 값이 주어졌기 때문에
nums[1] = 1
nums[2] = 3
for i in range(3, 301):
    nums[i] = nums[i-1] + 2*nums[i-2]
for tc in range(1,T+1):
    num = int(input())
    print(f'#{tc}', nums[num//10])



    #1 3 5 11 21 ? 85 # f(n) = f(n-1) + 2*f(n-2) / f(0) = 1 f(1) = 3