T = int(input())

for tc in range(1, T+1):
    N, D = map(int, input().split())
    box = list(map(int, input().split()))
    dump = list(map(int, input().split()))

    box.sort(reverse = True)
    dump.sort()

    i = 0
    j = 0
    sums = 0
    while i < N and dump:
        if box[i] <= dump[-1]:
            sums += box[i]
            dump.pop()
        i += 1
    print(f'#{tc}', sums)