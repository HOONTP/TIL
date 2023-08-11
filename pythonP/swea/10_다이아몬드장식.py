T = int(input())

for tc in range(1, T+1):
    sen = input() # 출력길이 len(sen)*4 + 1

    n = len(sen)
    print('.'+'.#..'*n)
    print('.'+'#.'*n*2)
    for i in sen:
        print(f'#.{i}.', end='')
    print('#')
    print('.'+'#.'*n*2)
    print('.'+'.#..'*n)
