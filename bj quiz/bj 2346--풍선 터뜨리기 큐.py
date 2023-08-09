import sys
input = sys.stdin.readline

N = int(input())
que_lst = [i for i in range(1,N+1)]
num_lst = list(map(int, input().split()))


# print(num_lst)
# print(que_lst)

result = []
i = 0
result.append(que_lst.pop(i))

while que_lst:
    j = num_lst.pop(i)
    if j >0:
        i += j-1
    elif j <0:
        i += j
    result.append(que_lst.pop(i))
    n = len(que_lst)
    while i >= n:
        if i >= n:
            i = i - n

    # print(num_lst)
    # print(que_lst)
    if len(que_lst) == 1:
        result.append(que_lst.pop())

print(*result)