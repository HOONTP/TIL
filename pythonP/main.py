from itertools import permutations


def permute(nums, start, end, result):
    if start == end:
        result.append(nums[:])
    else:
        for i in range(start, end):
            # 현재 위치의 값을 고정시킴
            nums[start], nums[i] = nums[i], nums[start]
            # 나머지 부분에 대해 재귀적으로 순열을 생성
            permute(nums, start + 1, end, result)
            # 다시 원래대로 돌려놓음 (백트래킹)
            nums[start], nums[i] = nums[i], nums[start]


N, K = map(int, input().split())

weightList = list(map(int, input().split()))
# 0 1 2   0 2 1   1 0 2   1 2 0   2 0 1   2 1 0 팩토리얼 개념이 뭔가 있었던거 같은데 왜 생각이
perList = list(permutations(weightList))

# 결과를 저장할 리스트
permutation_list = []

# 순열 생성 함수 호출
permute(weightList, 0, N, permutation_list)

cnt = 0
for per in perList:
    sumNum = 0
    for j in per:
        sumNum += j - K
        if sumNum < 0:
            break
    else:
        cnt += 1
print(cnt)
