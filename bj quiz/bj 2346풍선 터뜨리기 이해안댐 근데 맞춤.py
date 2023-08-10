import sys

input = sys.stdin.readline

N = int(input())
que_lst = [i for i in range(1, N + 1)]
num_lst = list(map(int, input().split()))

result = []
i = 0

while que_lst:
    result.append(que_lst.pop(i))
    j = num_lst.pop(i)
    # print(num_lst)
    # print(que_lst)
    if j > 0:
        i += j - 1
    elif j < 0:
        i += j

    # print(i)

    n = len(que_lst)
    while i >= n or i < 0:
        if i >= n:
            i = i - n

        elif i < 0:
            i = n + i

    # print(num_lst)
    # print(que_lst)
    if len(que_lst) == 1:
        result.append(que_lst.pop())

print(*result)


