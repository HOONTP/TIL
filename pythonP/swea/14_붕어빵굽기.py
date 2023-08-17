T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())

    lst = list(map(int, input().split()))
    lst.sort()


    i = 1
    que = 0
    result = 'Possible'
    j = 0

    for i in range(N):
        if (lst[i] // M)*K >= (i+1):
            continue
        else:
            result = 'Impossible'
            break
    print(f'#{tc}', result)
'''짧코 
for t in range(int(input())):
    N,M,K=map(int,input().split())
    l=sorted(map(int,input().split()))
    j=q=0
    r='Possible'
    for i in range(N):
        if (l[i]//M)*K<(i+1):
            r='Impossible'
            break
    print(f'#{t+1}', r)
'''
    #이건 왜 시간초과?
    # while j < N:
    #     if i % M == 0:
    #         que += K
    #     if i == lst[j]:
    #         if que > 0:
    #             que -= 1
    #             j += 1
    #         else:
    #             result = 'Impossible'
    #             break
    #     i += 1
    # print(f'#{tc}', result)