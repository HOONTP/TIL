import sys
input = sys.stdin.readline

N = int(input())
dics = {}
x_set = set()
for NN in range(N): # 값을 넣을 때 반복문을 돌리면서 크기에 따라 위치를 정한다면 순서대로 넣을 수 있지만
    x, y = map(int, input().split())# 그렇게하면 순회 횟수가 너무 많아짐
    if x not in x_set:
        x_set.add(x)
        INS = {x : [y]}
        dics.update(INS)
    elif x in x_set:
        dics[x].append(y)
# tuple로 .append(x, y)를
# sort_list.sort(key = lambda item: (item[0], item[1]))

x_= sorted(dics) # 딕셔너리를 sorted하면 키값만 뽑아서 정렬 리스트 만들어줌

for NNN in x_:
    dics[NNN].sort()

for i in x_:
    for ic in range(len(dics[i])):
        print(i, dics[i][ic])