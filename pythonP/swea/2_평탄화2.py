T = 10
def mnmx(lst):
    i = 99
    while lst[i] < lst[i-1]:
        lst[i], lst[i-1] = lst[i-1], lst[i]
        i -= 1

    j = 0
    while lst[j] > lst[j+1]:
        lst[j], lst[j+1] = lst[j+1], lst[j]
        j += 1
    return lst

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    for _ in range(N):
        lst[0] += 1
        lst[-1] -= 1
        lst = mnmx(lst)

    print(f'#{tc} {lst[-1]-lst[0]}')