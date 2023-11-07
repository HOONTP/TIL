def solution(today, terms, privacies):  # 1995.03.03 / A 1~100 / xxxx.xx.xx A /
    year = today[0:4]
    month = today[5:7]
    day = today[8:10]
    # print(year,month,day)

    answer = []
    for i in range(len(privacies)):
        sums = 0
        sums += (int(year) - int(privacies[i][0:4])) * 12 * 28
        sums += (int(month) - int(privacies[i][5:7])) * 28
        sums += (int(day) - int(privacies[i][8:10]))
        print(sums, privacies[i][-1], terms)
        for term in terms:
            if privacies[i][-1] in term:
                if int(term[2:]) * 28 <= sums:
                    answer.append(i + 1)
                    break

    return answer