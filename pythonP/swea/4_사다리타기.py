T = 10

for tc in range(1, T+1):
    input()
    lst = []
    for _ in range(100):
        lst_ = list(map(int, input().split()))
        lst.append(lst_)

    j = lst[99].index(2)

    i = 99 # (99, start_p) lst[i][j]
    while 0 < i:
        if j+1 <= 99 and lst[i][j+1] == 1:
            while j+1 <= 99 and lst[i][j+1] == 1:
                if j < 99:
                    j += 1
            i -= 1
        elif 0 <= j-1 and lst[i][j-1] == 1:
            while 0 <= j-1 and lst[i][j-1] == 1:
                if j > 0:
                    j -= 1
            i -= 1
        else:
            i -= 1
    print(j)