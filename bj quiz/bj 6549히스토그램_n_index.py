import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    N = arr[0]
    lst = arr[1:]
    if N == 0:
        break
    # print(N, lst)


    stack = [[0, lst[0], 0]]
    result = [0] * N
    # print(lst)
    i = N - 1# N이 1이 들어와버리면 for문 진행 안되고 터져버리는듯 항상 끝값 입력해보자.
    for i in range(1, N):
        if stack[-1][1] < lst[i]:
            stack.append([i, lst[i], i])
        elif stack[-1][1] == lst[i]:
            stack.append([stack[-1][0], lst[i], i])
        else:
            while stack:
                if stack[-1][1] > lst[i]:
                    result[stack[-1][0]] = max(result[stack[-1][0]], stack[-1][1] * (i - stack[-1][0]))
                    stack.pop()
                elif stack[-1][1] == lst[i]:
                    stack.append([stack[-1][0], lst[i], i])
                    break
                else:
                    stack.append([stack[-1][2]+1, lst[i], i])
                    break
            if not stack:
                stack.append([0, lst[i], i])
        # print(stack)

    #남은걸 어떻게 하지?
    while stack:
        result[stack[-1][0]] = max(result[stack[-1][0]], stack[-1][1] * (i - stack[-1][0] + 1))
        stack.pop()
    # print(result)
    print(max(result))
'''
스택에 담다가 [index, values] 작은 값이 나오면 pop하면서 값 저장 values * (now index - old index)하면 될듯?
'''