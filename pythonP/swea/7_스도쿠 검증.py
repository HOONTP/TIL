T = int(input())

def check(arr):
    num_set = {1,2,3,4,5,6,7,8,9}

    for i in range(9):
        if set(arr[i]) != num_set:
            return False

    for j in range(9):
        set_i = set()
        for i in range(9):
            set_i.add(arr[i][j])
        if set_i != num_set:
            return False

    for i in range(0,9,3):
        for j in range(0,9,3):
            set_sq = set()
            for k in range(3):
                for l in range(3):
                    set_sq.add(arr[i+k][j+l])
            if set_sq != num_set:
                return False
    return True


for tc in range(1, T+1):
    lst = [list(map(int, input().split())) for _ in range(9)]

    print(f'#{tc} {0+check(lst)}')