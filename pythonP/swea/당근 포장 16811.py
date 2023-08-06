import sys
sys.stdin = open('../input.in')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    new_lst = []

    aver = N/3
    i = 0
    cnt = 1

    while i < N:
        try:
            if lst[i] == lst[i+1]:
                cnt += 1
            else:
                new_lst.append(cnt)
                cnt = 1
            i += 1
        except IndexError:
            new_lst.append(cnt)
            i += 1

    print(new_lst, 'A')

    result = 0
    sums = 0
    j = 0
    sum_lst = []
    while True:
        if max(new_lst) > N/2:
            result = -1
            break

        while j < len(new_lst):
            if j == len(new_lst)-1:
                sums += new_lst[j]
                sum_lst.append(sums)
                break
            if sums + new_lst[j] < aver:
                sums += new_lst[j]
                j += 1
            elif sums + new_lst[j] > aver:
                if aver - sums > sums + new_lst[j] - aver:
                    sums += new_lst[j]
                    sum_lst.append(sums)
                    sums = 0
                    j += 2
                    aver = sum(new_lst[j:])/len(new_lst[j:])
                else:
                    sum_lst.append(sums)
                    sums = 0
                    j += 1
                    aver = sum(new_lst[j:])/len(new_lst[j:])
            else:
                sums += new_lst[j]
                sum_lst.append(sums)
                sums = 0
                j += 1
                aver = sum(new_lst[j:])/len(new_lst[j:])
        result_j = max(sum_lst) - min(sum_lst)
        print(sum_lst)
        k = len(new_lst)-1
        print(aver)
        sum_lst = []
        while k >= 0:
            if k == 0:
                sums += new_lst[k]
                sum_lst.append(sums)
                break
            if sums + new_lst[k] < aver:
                sums += new_lst[k]
                k -= 1
            elif sums + new_lst[k] > aver:
                if aver - sums > sums + new_lst[k] - aver:
                    sums += new_lst[k]
                    sum_lst.append(sums)
                    k -= 1
                    aver = sum(new_lst[:k+1])/len(new_lst[:k+1])
                else:
                    sum_lst.append(sums)
                    sums = 0
                    k -= 1
                    aver = sum(new_lst[:k+1])/len(new_lst[:k+1])
            else:
                sums += new_lst[k]
                sum_lst.append(sums)
                sums = 0
                k -= 1
                aver = sum(new_lst[:k+1])/len(new_lst[:k+1])

        print(sum_lst)
        result_k = max(sum_lst) - min(sum_lst)
        break

    result = min(result_j, result_k)
    print(f'#{tc}', result)

    # 1 1 1
    # 3 1 1
    # 1 1 1 1 1 1 1 1
    # 1 7 1 1 1 1 1 1 14 8 평균과 가장 가깝게 묶은 다음 다시 평균을 내서 평균과 가깝게 묶기
    # 순방향 역방향 차이 값 비교해서 작은 걸루