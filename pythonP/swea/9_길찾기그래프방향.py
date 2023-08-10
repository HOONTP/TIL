T = 10

def findroot(n, E, arr):
    stack = []
    visted = [0]*100
    while n < 99:
        for w in range(E):
            if arr[n][w] == 1 and visted[w] == 0:
                stack.append(n)
                n = w
                visted[n] = 1
                break
        else:
            if stack:
                n = stack.pop()
            else:
                return 0
    if n == 99:
        return 1
    return 2


for tc in range(1, T+1):
    a, E = map(int, input().split())
    nums = list(map(int, input().split()))
    arr = [[0]*100 for _ in range(100)]
    for i in range(E):
        arr[nums[2*i]][nums[2*i+1]] = 1

    print(f'#{tc}', findroot(0, 100, arr))