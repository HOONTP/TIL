dic_ = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

T = int(input())

for tc in range(1, T+1):
    N, A = input().split()
    result = ''
    for i in range(int(N)):
        a = dic_[A[i]]
        if a // 8:
            result = result + '1'
            a = a % 8
        else:
            result = result + '0'
        if a // 4:
            result = result + '1'
            a = a % 4
        else:
            result = result + '0'
        if a // 2:
            result = result + '1'
            a = a % 2
        else:
            result = result + '0'
        if a == 1:
            result = result + '1'
        else:
            result = result + '0'
    print(f'#{tc}', result)