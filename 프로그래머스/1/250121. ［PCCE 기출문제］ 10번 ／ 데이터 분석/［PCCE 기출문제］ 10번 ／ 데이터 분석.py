def solution(data, ext, val_ext, sort_by):

    num = check(ext)
    sortNum = check(sort_by)
    answer = []
    for datas in data:
        if datas[num] < val_ext:
            answer.append(datas)
    answer.sort(key=lambda x : x[sortNum])
    
    return answer

def check(X):
    num = 0
    if X == "code":
        num = 0
    elif X == "date":
        num = 1
    elif X == "maximum":
        num = 2
    elif X == "remain":
        num = 3
    return num