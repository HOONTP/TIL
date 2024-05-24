def solution(n, tops):  # %10007
    
    """
    이렇게하면 리스트에서 시간 복잡도 증가해서 시간초과 1개 뜸
    #     if tops[0] == 0:
    #         qudList = [2]
    #         triList = [3]
    #     else:
    #         qudList = [3]
    #         triList = [4]

    #     for i in range(1, n):
    #         if tops[i] == 1:
    #             qudList.append(qudList[i-1] + triList[i-1] * 2)
    #             triList.append(qudList[i] + triList[i-1])

    #         elif tops[i] == 0:
    #             qudList.append(qudList[i-1] + triList[i-1])
    #             triList.append(qudList[i] +triList[i-1])

    #     answer = triList[-1] % 10007
    """
    # if tops[0] == 0:
    #         qudL = 1
    #         triL = 1
    # else:
    #         qudL = 1
    #         triL = 1
    # 
    # for i in range(n):
    if tops[0] == 0:
        qudL = 2
        triL = 3
    else:
        qudL = 3
        triL = 4

    for i in range(1, n):
        if tops[i] == 1:
            qudL = qudL + triL * 2
            triL = qudL + triL

        elif tops[i] == 0:
            qudL = qudL + triL
            triL = qudL + triL

    answer = triL % 10007
    return answer