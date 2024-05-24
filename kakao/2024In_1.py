def solution(friends, gifts):
    N = len(friends)
    dic = dict()
    givePoint = [0 for _ in range(N)]
    getItem = [0 for _ in range(N)]
    giveMap = [[0 for _ in range(N)] for __ in range(N)]
    i = 0
    for name in friends:
        dic[name] = i
        i += 1
    # print(dic)
    for st in gifts:
        a, b = st.split(" ")
        giveMap[dic[a]][dic[b]] += 1
        givePoint[dic[a]] += 1
        givePoint[dic[b]] -= 1
    # print(giveMap)
    # print(givePoint)

    for i in range(N):
        for j in range(N):
            if i >= j: continue
            give = giveMap[i][j]
            rece = giveMap[j][i]
            if give > rece:
                getItem[i] += 1
            elif give == rece:
                if givePoint[i] > givePoint[j]:
                    getItem[i] += 1
                elif givePoint[j] > givePoint[i]:
                    getItem[j] += 1
                else:
                    continue
            else:
                getItem[j] += 1

    # print(getItem)
    answer = max(getItem)
    return answer