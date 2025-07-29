def solution(arr):
    answer = [arr[0]]

    for ar in arr:
        if answer[-1] == ar:
            continue
        else:
            answer.append(ar)
        
    return answer