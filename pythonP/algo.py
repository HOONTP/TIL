import sys
input = sys.stdin.readline

def binary(arr, n, E):
    start = 0
    end = E - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < n:
            start = mid + 1
        elif arr[mid] > n:
            end = mid - 1
        else:
            return -1
    return start


N = int(input())

lst = list(map(int, input().split()))
stack = [lst[0]]
s_end = 1
results = []
results.append([stack, 1])
for i in lst:
    for j in range(s_end):
        if results[j][0][-1] < i:
            results[j][1] += 1
            results[j][0].append(i)
        elif results[j][0][-1] > i:
            change = binary(results[j][0], i, results[j][1])
            if change != -1:
                new = results[j][0][:change]
                new.append(i)
                results.append([new, change+1])
                s_end += 1
    leng = s_end
    for k in range(leng-1, 0, -1):
        if results[k-1][1] <= results[k][1]:
            results.pop(k-1)
            s_end -= 1
        print(results)
target = 0
value = 0
for i in range(s_end):
    if value < results[i][1]:
        target = i
        value = results[i][1]

print(value)
print(*results[target][0])