T = int(input())

# for tc in range(1, T+1): #부모 인덱스로 저장
#     E, N = map(int, input().split())
#
#     lst = list(map(int, input().split()))
#     tre = [0]*(E+2)
#     print(tre)
#     print(lst)
#
#     for i in range(0, 2*E, 2):
#         tre[lst[i+1]] = lst[i]
#     print(tre)
def tre_cnt(n):
    global cnt
    cnt += 1
    if c1[n] != 0:
        tre_cnt(c1[n])
    if c2[n] != 0:
        tre_cnt(c2[n])

for tc in range(1, T+1):#자식 인덱스를 저장 c1 c2
    E, N = map(int, input().split())

    lst = list(map(int, input().split()))
    c1 = [0]*(E+2)
    c2 = [0]*(E+2)
    for i in range(0, 2*E, 2):
        if c1[lst[i]] == 0:
            c1[lst[i]] = lst[i+1]
        elif c1[lst[i]] != 0:
            c2[lst[i]] = lst[i+1]
    cnt = 0
    tre_cnt(N)
    print(f'#{tc}', cnt)