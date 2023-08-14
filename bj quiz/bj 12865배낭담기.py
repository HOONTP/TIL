N, K = map(int, input().split())

count = [0]*(K+1)
arr = []
for _ in range(N):
    w, v = map(int, input().split())
    arr.append((w,v))

arr.sort()
# print(arr)
for i in arr:
    for j in range(K, -1, -1):#뒤에서 부터 해야함!
        if i[0] + j < K+1:
            count[i[0] + j] = max(i[1]+count[j], count[i[0] + j])
    # print(count)
print(max(count))