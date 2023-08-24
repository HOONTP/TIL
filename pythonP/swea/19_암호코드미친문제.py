# 이거는 변환만 해준다.
first_ = ['0000', '0001', '0010', '0011', '0100', '0101',
              '0110', '0111', '1000', '1001', '1010', '1011',
              '1100', '1101', '1110', '1111']
def make_code(): # 본 코드를 2진수로 바꾸는 함수
    for long in code_:
        G = ''
        for al in long:
            if al == '0':
                G = G + first_[0]
            elif al == '1':
                G = G + first_[1]
            elif al == '2':
                G = G + first_[2]
            elif al == '3':
                G = G + first_[3]
            elif al == '4':
                G = G + first_[4]
            elif al == '5':
                G = G + first_[5]
            elif al == '6':
                G = G + first_[6]
            elif al == '7':
                G = G + first_[7]
            elif al == '8':
                G = G + first_[8]
            elif al == '9':
                G = G + first_[9]
            elif al == 'A':
                G = G + first_[10]
            elif al == 'B':
                G = G + first_[11]
            elif al == 'C':
                G = G + first_[12]
            elif al == 'D':
                G = G + first_[13]
            elif al == 'E':
                G = G + first_[14]
            elif al == 'F':
                G = G + first_[15]
        get_nd.append(G)

# 이게 비율로 들어가야 된다. 왜 why
dic_o = ['0001101', '0011001', '0010011', '0111101', '0100011',
        '0110001', '0101111', '0111011', '0110111', '0001011']
# 배율 업! 새로운 dic을 만든다.
def up(p): # dic_o 의 값들을 계속해서 불려주는 함수
    new_dic = [] # 배율 p라 치고
    for i in range(10):
        mid = ''
        for w in dic_o[i]:
            mid = mid + w*p # 각 문자열에 배율p 만큼 곱해서 다시 담기,
        new_dic.append(mid)
    return new_dic

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = [input() for _ in range(N)]
    check = ['0' for _ in range(M)] # 모든게 0 으로 이루어진 줄 빼기 위한 변수
    check = ''.join(check)
    code = set()
    for i in A:
        if i != check:
            code.add(i)# 0이 아닌 모든 줄 code(set)에 담아준다.
    code_ = list(code)
    get_nd = []
    total = set()
    make_code()# 위에서 만든 2진수 생성 함수

    for full in get_nd:
        result = []
        m = len(full) - 1
        F = 0
        p = 1
        i = m
        while 7*8*p < m: # 8자리 7칸 배율p 가 총 길이보다 길어지면 탈출
            dic_ = up(p) # 배율적용 1배율 부터

            while 0 <= i:
                n = full[i-7*p+1:i+1] # 뒤에서 부터 한칸씩 탐색
                if n in dic_: # 코드와 겹치는 구간 발생시 진입
                    while 0 <= i:
                        a = full[i-7*p+1:i+1]
                        for k in dic_: # 어떤 코드와 겹치는지 검토
                            if k == a:
                                result.append(dic_.index(k))
                                i -= 7*p # 코드를 찾았으니 앞으로 점프
                                break
                        else: # 더이상 같은게 없을 때
                            if len(result) == 8: # 담은 result길이가 8이면
                                result = tuple(result) # tuple 형태로 담는다
                                total.add(result) # set에는 list가 담기지 않음.
                            result = [] #result 리셋
                            break
                i -= 1
            result = []
            p += 1 # 배율 증가
            i = m # i 값 리셋

    total = list(total)
    mx_sum = 0

    for fin in total: # 코드 검증
        sums = 0
        for i in range(3, -1, -1):# 뒤에서 부터 담아서 홀 짝 바꿈
            sums += fin[i*2+1]*3
            sums += fin[i*2]
        if sums % 10 == 0:
            mx_sum += sum(fin) # 검증된 값 저장

    if mx_sum == 0:
        print(f'#{tc}', 0)
    else:
        print(f'#{tc}', mx_sum)
