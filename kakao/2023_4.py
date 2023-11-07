import sys
input = sys.stdin.readline

numbers = list(map(int, input().split())) # 프로그래머스 디버깅 안 좋다 ...
def solution(numbers):
    # 7 3 3 1 1 / 15 7 7 3 3 1 1 / 31 ,, 2^n-1
    answer = []
    def scanTree(nums, start, end): # 1101111 , 0 , 6 / c = 3 / 0 1 2 / 4 5 6 / 0 / 2 / 4 / 6
        center = start + (end - start) // 2
        # print(start,center, end)
        if start == end:
            return True
        else:
            if nums[center] == '1':
                left = scanTree(nums, start, center-1)
                right = scanTree(nums, center+1, end)
            else:
                if '1' not in nums[start:end+1]:
                    print(start, end)
                    return True
                else:
                    return False
        if left and right:
            return True
        else:
            return False

    for number in numbers: # 이걸 어떻게 2**n -1개로 맞춰줄까
        num2 = bin(number)
        num = num2[2:]
        N = len(num)
        for i in range(1, 7):
            n = (2**i)-1
            if N <= n:
                break
        # i 는 2**n-1에서 n값
        num = ((2**i - 1)-N)*'0' + num
        N = len(num) # 000000)1101111 N-1개까지 붙여짐
        # print(num, N)
        isTree = scanTree(num, 0, N-1)
        if isTree == True:
            answer.append(1)
        else:
            answer.append(0)
    # print(len(bin(10**15)))
    return answer
print(solution(numbers))