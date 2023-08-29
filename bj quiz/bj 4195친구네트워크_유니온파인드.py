import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9) #그냥 이런식으로 깊이를 넓히는게 어딧냐고;

def find(x):
    global cnt
    # print(x, dic_)
    # cnt += 1
    if dic_[x] != x:
        dic_[x] = find(dic_[x])
        # cnt += point[x]
        # point[x] = cnt
    return dic_[x]

T = int(input())

for _ in range(T):
    N = int(input())
    dic_ = {}
    point = {}
    for _ in range(N):
        a, b = input().split()
        if dic_.get(a) == None and dic_.get(b) == None:
            dic_[a] = a + b
            dic_[b] = a + b
            dic_[a+b] = a + b
            point[a] = 1
            point[b] = 1
            point[a+b] = 2
            print(2)
        elif dic_.get(b) == None:
            cnt = 0
            A = find(a)
            dic_[b] = a
            point[A] += 1
            print(point[A])
        elif dic_.get(a) == None:
            cnt = 0
            B = find(b)
            dic_[a] = b
            point[B] += 1
            print(point[B])
        else:
            cnt = 0
            A = find(a)
            B = find(b)
            if A != B:
                dic_[A] = B
                total = point[A] + point[B]
                point[A] = total
                point[B] = total
                print(total)
            else:
                print(point[A])