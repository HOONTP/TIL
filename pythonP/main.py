def solution(numbers):
    # 646 64(5)  -> 646 64
    # 464 46(5)  -> 46 464
    # 322 32(2)  -> 32 322
    # 244 24(4)  -> 244 24 1번이 2번보다 작으면 큰수순?
    # 58 5 58 5
    # 
    # 445 
    # numbers = [100, 999, 989, 9, 98, 988, 0, 85, 8, 8, 586, 5, 58, 586, 576, 556, 554,646, 64, 464, 46,1000, 1, 15, 23, 32, 322, 232]
    # 33 3 

    num_lst = [[[[] for _ in range(10)] for _ in range(10)] for _ in range(10)]

    for num in numbers:
        len_str = str(num)
        if len(len_str) == 1:
            num_lst[9 - num][9 - num][9 - num].append(len_str)
        elif len(len_str) == 2:
            num_lst[9 - num // 10][9 - num % 10][9 - num // 10].append(len_str)
        elif len(len_str) == 3:
            num_lst[9 - num // 100][(9 - num // 10) % 10][9 - num % 10].append(len_str)
        else:
            num_lst[9][9][9].append(len_str)
    # print(num_lst)
    num_lst[9][9][9].sort(reverse=True)
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if i > j:
                    num_lst[i][j][k].sort()
                elif i < j:
                    num_lst[i][j][k].sort(reverse=True)
                num_lst[i][j][k] = ''.join(num_lst[i][j][k])
    # print(num_lst)
    for i in range(10):
        for j in range(10):
            num_lst[i][j] = ''.join(num_lst[i][j])
    # print(num_lst)
    for i in range(10):
        num_lst[i] = ''.join(num_lst[i])
    # print(num_lst)
    answer = ''.join(num_lst)
    # print(answer)
    if int(answer) == 0:
        answer = '0'
    return answer