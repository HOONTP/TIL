import sys
input = sys.stdin.readline

S = input().strip()

def get_subsets(nums):
    n = len(nums)
    subsets = []

    def generate_subset(index, subset):
        if index == n:
            if subset not in subsets: #True로 해도 같나?
                subsets.append(subset)
                return
            else:
                return
        generate_subset(index + 1, subset + [nums[index]])  # 원소를 선택한 경우
        generate_subset(index + 1, subset)  # 원소를 선택하지 않은 경우
    generate_subset(0, [])
    return subsets

print(S)
subsets = get_subsets(S)
print(subsets)
print(len(subsets))