import sys
input = sys.stdin.readline

# for i, j in memo:  # 유니온파인드는 출력 or 분해 작업 시 동기화 필수인듯. 복잡도 크지 않으니.
#     unionFind([i, j])
commands = input().split('", "')
print(commands)
def solution(commands): # 최대 2500 * 1000 = 2500000 정도?
    # 아에 다 순회하지말고 값이 있는 애들을 따로 관리하는건 어떤지 set에 담아서 탐색 시 순회?
    def unionFind(x):
        if union[x[0]][x[1]] == x:
            return x
        union[x[0]][x[1]] = unionFind(union[x[0]][x[1]])
        return union[x[0]][x[1]]
    def merge(a, b):
        if a == b:
            return
        memo.add((a[0],a[1]))
        memo.add((b[0],b[1]))
        A = unionFind(a)
        B = unionFind(b)
        if A != B:
            if table[A[0]][A[1]]:
                union[B[0]][B[1]] = A
            else:
                union[A[0]][A[1]] = B
        return
    def update(lst):
        if len(lst) == 3:
            i = int(lst[0])
            j = int(lst[1])
            X = unionFind([i,j])
            table[X[0]][X[1]] = lst[2]
            memo.add((X[0], X[1]))
        else:
            if lst[0] == lst[1]:
                return
            else:
                for i, j in memo:
                    X = unionFind([i, j])
                    if table[X[0]][X[1]] == lst[0]:
                        table[X[0]][X[1]] = lst[1]
        return
    def unmerge(x):
        for i, j in memo: # 유니온파인드는 출력 or 분해 작업 시 동기화 필수인듯. 복잡도 크지 않으니.
            unionFind([i, j])
        X = unionFind(x)
        if table[X[0]][X[1]]:
            # print(X, x, table[X[0]][X[1]])
            table[x[0]][x[1]] = table[X[0]][X[1]]
            union[x[0]][x[1]] = [x[0], x[1]]
        else:
            union[x[0]][x[1]] = [x[0], x[1]]
        for i, j in memo:
            unionFind([i, j])
        for i, j in memo:
            if unionFind([i, j]) == X:
                if [i, j] != x:
                    table[i][j] = ''
                    union[i][j] = [i, j]
        return
    answer = []
    memo = set()
    union = [[[i, j] for j in range(51)] for i in range(51)]
    # print(union)
    table = [['']*51 for _ in range(51)]
    # print(table)
    for command in commands:
        com = command.split()
        print(com)
        if com[0] == 'UPDATE':
            update(com[1:])
        elif com[0] == 'MERGE':
            data = com[1:]
            r1, c1, r2, c2 = map(int, data)
            merge([r1,c1], [r2,c2])
        elif com[0] == 'UNMERGE':
            unmerge([int(com[1]), int(com[2])])
        else:
            i = int(com[1])
            j = int(com[2])
            X = unionFind([i, j])
            if table[X[0]][X[1]]:
                answer.append(table[X[0]][X[1]])
            else:
                answer.append("EMPTY")
        for i in range(1, 5):
            print(table[i][1:5])
            print(union[i][1:5])
        print()

    return answer
result = solution(commands)
print(result)