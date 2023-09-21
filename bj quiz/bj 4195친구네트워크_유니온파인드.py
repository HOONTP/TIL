import sys
input = sys.stdin.readline

def find(x):
    if dic_[x] != x:
        dic_[x] = find(dic_[x])
    return dic_[x]

T = int(input())

for _ in range(T):
    sb = []
    N = int(input())
    dic_ = {}
    point = {}
    for _ in range(N):
        a, b = input().split()
        if dic_.get(a) == None and dic_.get(b) == None:
            dic_[a] = a
            dic_[b] = a
            point[a] = 2
            sb.append(2)
        elif dic_.get(b) == None:
            A = find(a)
            dic_[b] = A
            point[A] += 1
            sb.append(point[A])
        elif dic_.get(a) == None:
            B = find(b)
            dic_[a] = B
            point[B] += 1
            sb.append(point[B])
        else:
            A = find(a)
            B = find(b)
            if A != B:
                dic_[A] = B
                total = point[A] + point[B]
                point[A] = total
                point[B] = total
                sb.append(total)
            else:
                sb.append(point[A])
    print(*sb)