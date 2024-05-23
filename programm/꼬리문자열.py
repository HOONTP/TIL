def solution(str_list, ex):
    for i in range(len(str_list)):
        if ex in str_list[i]:
            str_list[i] = ''
    print(str_list)
    answer = ''.join(str_list)
    return answer