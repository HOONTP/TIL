import sys
input = sys.stdin.readline

def tool(SET, *parm):
    if parm[0] == 'add':
        SET.add(parm[1])
        return SET
    if parm[0] == 'remove':
        SET.discard(parm[1])
        return SET
    if parm[0] == 'check':
        if parm[1] in SET:
            print('1')
        else:
            print('0')
        return SET
    if parm[0] == 'toggle':
        if parm[1] in SET:
            SET.remove(parm[1])
        else:
            SET.add(parm[1])
        return SET
    if parm[0] == 'all':
        SET = {'1', '2', '3', '4', '5', '6', '7', '8','9','10','11','12','13','14','15','16','17','18','19','20'}
        return SET
    if parm[0] == 'empty':
        SET = set()
    return SET

M = int(input())
S = set()

for _ in range(M):
    input_ = input()
    split_ = input_.split()
    if len(split_) == 2:
        S = tool(S, split_[0], split_[1])
    else:
        S = tool(S, split_[0])

# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다. 