T = int(input())

def get_subsets(nums):
    n = len(nums)
    subsets = []

    def generate_subset(index, subset):
        if index == n:
            if subset not in subsets:
                subsets.append(subset)
                return
            else:
                return
        generate_subset(index + 1, subset + [nums[index]])
        generate_subset(index + 1, subset)

    generate_subset(0, [])
    return subsets

S = [i for i in range(1, 13)]
subsets = get_subsets(S)

for tc in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0
    md_s = 0

    for i in subsets:
        if len(i) == N and sum(i) == K:
            cnt += 1

    print(f'#{tc} {cnt}')