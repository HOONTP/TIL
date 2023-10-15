import sys
input = sys.stdin.readline

def binary(arr, n):
    start = 0
    end = s_end - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < n:
            start = mid + 1
        elif arr[mid] > n:
            end = mid - 1
        else:
            return -1
    return start
'''
새로운 수를 가장긴 상태인 리스트에서 최적의 자리에 심어준다는 느낌
'''

N = int(input())

lst = list(map(int, input().split()))
# stack = [[] for _ in range(N)] # stack을 떠올렸지만 스택으로 쓰진 않음.
stack = []
stack.append((0, lst[0]))

print(stack)
for i in lst:
    if stack[-1]:
        stack[j][0] += 1
        stack[j][1].append(i)
        # elif stack[j][1][-1] > i:
        #     change = binary(stack, i)
        #     if change != -1:
        #         stack[change] = i
    else:
        stack.append([1,[i]])

# print(stack)
print(stack[0][0])
print(*stack[0][1])