import sys
input = sys.stdin.readline

sen = input().strip()
boom = input().strip()
n_count = len(boom)
stack = []
for i in sen:
    stack.append(i)
    if i == boom[-1]:
        if ''.join(stack[-n_count:]) == boom:# [index:] 에서는 index가 범위를 넘어도 ㄱㅊ 모두 추출
            for _ in range(n_count):
                stack.pop()
if stack:
    print(''.join(stack))
else:
    print("FRULA")


'''
방향에 따라 4^5회의 경우의 수가 나옴
진행 방향으로 모든 수를 다 옮겨야하니, 방향벡터를 인자로 받는 함수가 있으면 좋을듯.
진행 할 방향에서부터 순회가 들어가야함 그래야 먼저 합쳐지는 애들부터 순회
벽은 패스 그 다음인자를 순회하다가 0이 아닌 수를 만나면 해당 자리를 0으로 바꾸고
0이 아닌 수 혹은 벽을 만날 때까지 탐색하다가 만나는 순간 같은 수라면 그 자리에 더하고
아니라면 제자리.
'''
