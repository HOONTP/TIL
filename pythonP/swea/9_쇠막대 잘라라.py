T = int(input())

for tc in range(1, T+1):
    stack = [0]*50000
    sample = input()
    cnt = 0
    top = 0

    for i in range(len(sample)):
        if sample[i] == '(':
            top += 1
            stack[top] = sample[i]
        else:
            if stack and sample[i-1] == '(':
                top -= 1
                cnt += top
            else:
                top -= 1
                cnt += 1
    print(f'#{tc}', cnt)