import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

# print(lst)
'''
스택에 담았다 치고 다음 i 에서 스택으로 역추적하면 나보다 큰넘이 나올때까지 계속 카운팅 해야함

n과 j를 저렇게 기용한 이유는 len함수를 쓰지 않고 스택의 길이를 관리하고 싶어서,
'''
stack = []
cnt = 0
n = 0 # 스택의 길이를 관리
for i in lst:
    j = -1
    if stack:
        equal = 0
        while -j <= n:
            # print(stack, j, n, i)
            if stack[j][0] < i:
                cnt += stack[j][1]
                stack.pop()
                n -= 1
            elif stack[j][0] == i: # 만약 같아서 해당 길이의 개수를 늘렸다면 equal에 1을 더해서 더 큰 사람을 만났을 때 고려해줄 것
                cnt += stack[j][1]
                stack[j][1] += 1
                j -= 1
                equal += 1
            else:
                if equal:  # 이미 사용된 경우 카운팅만 해준다. ( 사용된 경우 스택에 담겨 있음. )
                    cnt += 1
                else:
                    cnt += 1 # 같은 적이 없어서 사용되지 않은 경우라면 카운팅 뿐 아니라 스택에 담아 준다.
                    stack.append([i, 1])
                    n += 1
                break
    if not stack: # 중간에 스택이 모두 빠지는 경우가 발생하기때문에 위로 빼주면 안돌아가는듯. ( 현재 수가 가장 커서 모든 스택 제거 했을 경우 )
        stack.append([i, 1])
        n += 1
print(cnt)