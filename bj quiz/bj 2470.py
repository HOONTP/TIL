import sys
input = sys.stdin.readline

N = int(input())

lists = list(map(int, input().split()))
lists.sort()
set_list = set(lists)
num_list = []

def first_case():
    if len(lists) == 2:
        return lists[0], lists[1]
    elif len(lists) == 1:
        return lists[0]
    i = 0
    while i < N-1 and lists[i] < 0:
        if abs(lists[i]) in set_list:
            return lists[i], abs(lists[i]) # 절대 값이 같은 수가 있다면 결과는 0 10만회
        i += 1
    # print(lists)
    if lists[0] >= 0:
        return lists[0], lists[1]
    elif lists[N-1] <= 0:
        return lists[N-2], lists[N-1]
    it = N-1
    for ic in range(N):
        while abs(lists[ic]+lists[it]) > abs(lists[ic]+lists[it-1]) and ic != it-1:
            it -= 1
        num_list.append((lists[ic],lists[it]))
            # print(lists[ic],lists[it])
    return (num_list)

case_list = first_case()
result = 1000000000
sum_case = 0
result_case = []

if isinstance(case_list, tuple):
    print(case_list[0], case_list[1])
else:
    for re in case_list:
        if re[0] == re[1]:
            case_list.remove(re)
    for NN in case_list:
        sum_case = NN[0] + NN[1]
        if abs(sum_case) < result:
            result = abs(sum_case)
            result_case = [NN[0], NN[1]]
        result_case = sorted(result_case)
    print(result_case[0], result_case[1])



#10만개
# 차이가 난다면? 1이상 10억 이하의 숫자인데 

# abs가 제일작은큰 음수 양수 끼리 차이와 각각의 수 2개의 abs합 총 3가지 비교

"""
1. 제일 처음에 양수만 혹은 음수만 있을 경우 먼저 출력
2. abs(-i) 랑 같은게 있다면 출력?
"""
"""
하나의 변수 => 가장 차이가 적은 상대값 도출 => 저장
( 값이 커지는 순간 멈추기 + 이전 인덱스가 짝인 인덱스 다음부터 시작 )
0 -- > 99998
1 -- > 99998~비교
첫 값 < 다음 값 => 첫 값 기준으로 각 데이터 저장 + 반대쪽 인덱스 유지
"""