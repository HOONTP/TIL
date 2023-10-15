import sys
input = sys.stdin.readline

def binary(arr, n):
    start = 0
    end = size - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid][-1] < n:
            start = mid + 1
        elif arr[mid][-1] > n:
            end = mid - 1
        else:
            return mid
    return start
'''
새로운 수를 가장긴 상태인 리스트에서 최적의 자리에 심어준다는 느낌
'''
def binaryreverse(arr, n):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] >= n:
            start = mid + 1
        elif arr[mid] < n:
            end = mid - 1
    return start
N = int(input())

lst = list(map(int, input().split()))
stack = [[lst[0]]] # stack을 떠올렸지만 스택으로 쓰진 않음.
size = 1

for i in lst:
    if stack[-1][-1] < i:
        size += 1
        stack.append([i])
    elif stack[-1][-1] > i:
        change = binary(stack, i)
        stack[change].append(i)

result = [stack[-1][-1]]

# size = 2
if size > 1:
    for j in range(size-2, -1, -1):
        if stack[j][0] < result[-1]:
            result.append(stack[j][0])
        else:
            ans = binaryreverse(stack[j], result[-1])
            result.append(stack[j][ans])
        # i = 0
        # while True:
        #     if stack[j][i] < result[-1]:
        #         result.append(stack[j][i])
        #         break
        #     i += 1
# print(result)
# print(stack)

print(size)
for k in range(size-1, -1, -1):
    print(result[k], end=' ')