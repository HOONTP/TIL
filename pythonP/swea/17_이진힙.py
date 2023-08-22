T = int(input())
'''
삽입을 위해선 탐색을 해야함. X
1부터 쭉 훑으면서 0 인 순간 입력하도록. X
+ 교환  X
=> 그냥 마지막에 추가 후 위와 비교하면서 교환
'''
def change(tre):#규칙이 성립 안될 때 교환하는 게 필요 한데 ,,
    N = len(tre) - 1
    i = 1
    while i < N:
        if i*2 <= N and tre[i] > tre[i*2]:
            tre[i], tre[i*2] = tre[i*2], tre[i]
            i = 1
        if i*2+1 <= N and tre[i] > tre[i*2+1]:
            tre[i], tre[i*2+1] = tre[i*2+1], tre[i]
            i = 1
        i += 1
'''
정석 아닌거 같은 데
마지막 노드부터 부모노드리스트에서 //2의 값과 비교하는게 더 짧고 간결할 듯.
'''

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    tre = [0]

    for i in range(N):
        # tre[i] = lst[i-1]
        tre.append(lst[i])
        change(tre)

    sums = 0
    i = N
    while i > 0:
        sums += tre[i//2]
        i = i//2
    print(f'#{tc}', sums)