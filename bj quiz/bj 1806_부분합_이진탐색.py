import sys
input = sys.stdin.readline

def binary(arr, n):
    start = n
    end = N - 1
    if arr[N-1] - arr[n] + lst[n] < S:
        return False

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] - arr[n] + lst[n] < S:
            start = mid + 1
        elif arr[mid] - arr[n] + lst[n] > S:
            end = mid - 1
        else:
            return mid - n + 1
    return start - n + 1

N, S = map(int, input().split())

lst = list(map(int, input().split()))
arr = [0]*N
arr[0] = lst[0]
for i in range(N-1):
    arr[i+1] = arr[i] + lst[i+1]

answer = float('inf')
for i in range(N):
    result = binary(arr, i)
    if result and result < answer:
        answer = result
        if answer == 1:
            break

if answer == float('inf'):
    print(0)
else:
    print(answer)