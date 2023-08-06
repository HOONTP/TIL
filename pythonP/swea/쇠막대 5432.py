T = int(input())

for tc in range(1, T+1):
    lst = input()

    new_lst = []
    for i in range(len(lst)): # ()()()() 녀석들 1,2,3 으로 치환[ (, (), ) ]
        if lst[i] == '(':
            if lst[i+1] != ')':
                new_lst.append(1)
            else:
                new_lst.append(2)
        elif lst[i] == ')':
            if lst[i-1] != '(':
                new_lst.append(3)
        else: # ()에서 ) 부분 패스
            pass

    result = new_lst.count(1)# 총 1의 개수 count의 시잡도 n
    cnt = 0
    for j in range(len(new_lst)):
        if new_lst[j] == 2: # 2일 경우 왼쪽의 (1갯수 - 3갯수) = 잘리는 막대 갯수 = 생기는 막대 개수
            result += cnt
        elif new_lst[j] == 1: # 1 카운트
            cnt += 1
        else: # 3 카운트
            cnt -= 1
    print(f'#{tc}', result)


    # () ( ( ( () () ) ( () ) () ) ) ( () ) 5개의 조각 / 2*3 1*3 1*2 1*1 => 17
    # 2 / 1 1 1 2 2 3 1 2 3 2 3 3 1 2 3
    # ( ( ( () ( () () ) ) ( () ) () ) ) ( () () ) 레이저 7 6조각 # 그럼 기본 갯수는? 1의 갯수
    # 1 1 1 2  1 2  2  3 3 1 2  3 2 3 3  1 2 2 3 # 1 - 3 cnt해서 2번일 때 * 해주면 추가되는 갯수