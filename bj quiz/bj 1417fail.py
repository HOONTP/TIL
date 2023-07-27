import sys
input = sys.stdin.readline

N = int(input())
lists = []
for _ in range(N):
    M = int(input())
    lists.append(M)

ave = sum(lists)/len(lists)
ave_ = (sum(lists)-1)/len(lists)
print(int(ave))
print(int(ave_))
ave = int(ave)

def need_num(aver, aver_):
    if len(lists) == 1:
        return 0
    if max(lists) == lists[0]:
        return 0
    if lists[0] <= aver:
        for i in lists:
            if abs(i - aver) > aver + 2 - lists[0]:
                if i -lists[0] % 2 == 1:
                    return int((i-lists[0]-1)/2)+1
                else:
                    return int((i-lists[0])/2)+1
        if aver == aver_:
            return aver + 1 - lists[0]
        elif aver == int(aver_):
            return aver + 2 - lists[0]
        else:
            return aver + 1 - lists[0]
    
print(need_num(ave, ave_))

# 내림하고 2개 가져가기 or 1개로 숫자가 작아지면 1개만 가져가기 인데

# 1번이 주인공 나머지 인원에게서 몇개를 뺏어와야 하는지 
# 모든 인원의 평균을 낸다. => 나머지의 합을 구한다. 2를 가져오고 나머지는 분배하면 된다.
# 나눠줬을 때 1 이상이면 평균이 되고 / 차 가 1 이면 1개만 택하고 아니면 2개를 택하면 되긴하는데..
# N 50 M 100