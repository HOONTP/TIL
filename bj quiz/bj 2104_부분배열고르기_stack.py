import sys
input = sys.stdin.readline
'''
본인이 최소값이 되는 경우에 가질 수 있는 가장 큰 구간합은 몇 인가?

남은 스택 고려하는 거랑 N 이 1인 경우처럼 for문 안돌아갈 경우 고려해서 반례 넣어보기.
'''
N = int(input())
lst = list(map(int, input().split()))
arr = [0]*N
arr[0] = lst[0]
for i in range(1, N):
    arr[i] = arr[i-1] + lst[i]

stack = [[lst[0], 0, 0]]
# result = [0]*N
mx = 0
i = N - 1
for i in range(1, N): # stack에는 [value, 계산ind, 찐index]의 형식? / arr[j] - arr[i] + lst[i]
    if lst[i] > stack[-1][0]:  # 현재 값이 더 크면 최소값은 유지 된다. 그리고 현재 값의 인덱스는 현재값으로 들어가면 된다.
        stack.append([lst[i], i, i])
    elif lst[i] == stack[-1][0]:
        stack.append([lst[i], stack[-1][1], i])
    else:
        while stack:
            # print(stack)
            # print(result)
            if lst[i] > stack[-1][0]: # stack을 제거 중에 현재보다 작은 값을 만나면 여기서 멈춰야함.
                stack.append([lst[i], stack[-1][2]+1, i]) # 그 값의 찐덱스보다 1칸 뒤부터시작,
                break
            elif lst[i] == stack[-1][0]:
                stack.append([lst[i], stack[-1][1], i])
                break
            else: # 현재 값이 더 작은 경우 이미 들어간 스택의 값들이 최소값을 위협받음.
                n = stack.pop() # value, index
                mid = (arr[i-1] - arr[n[1]] + lst[n[1]]) * n[0]
                if mx < mid:
                    mx = mid
                # result[n[2]] = (arr[i-1] - arr[n[1]] + lst[n[1]]) * n[0]
                # print(n, i, (arr[i-1], arr[n[1]],lst[n[1]]) ,n[0])
    if not stack:
        stack.append([lst[i], 0, i])

while stack: # i는 마지막 인덱스 ( N - 1 )
    n = stack.pop()
    mid = (arr[i] - arr[n[1]] + lst[n[1]]) * n[0]
    if mx < mid:
        mx = mid

print(mx)