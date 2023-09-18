import sys
input = sys.stdin.readline

T = int(input())

def merge_split(start, end):
    if start < end:
        n = end - start + 1
        mid = start + n//2 - 1

        merge_split(start, mid)
        merge_split(mid+1, end)

        merge(start, mid, end)
    return

def merge(left, mid, right):
    global cnt

    if lst[mid] > lst[right]:
        cnt += 1
    i = left
    j = mid+1
    k = left
    while (i <= mid) and (j <= right):
        if lst[i] <= lst[j]:
            arr[k] = lst[i]
            i += 1
            k += 1
        else:
            arr[k] = lst[j]
            j += 1
            k += 1
    while i <= mid:
        arr[k] = lst[i]
        i += 1
        k += 1
    while j <= right:
        arr[k] = lst[j]
        j += 1
        k += 1
    lst[left:right+1] = arr[left:right+1]

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    arr = [0] * N
    cnt = 0
    merge_split(0, N-1)

    print(f'#{tc} {lst[N//2]} {cnt}')