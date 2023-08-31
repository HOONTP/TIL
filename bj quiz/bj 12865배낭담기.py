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
        if i[0] + j < K+1:    # i의 무게와 더 할 수 있는 무게의 index에 아래 값을 넣자.
            count[i[0] + j] = max(i[1]+count[j], count[i[0] + j]) # i[1]와 더 할 수 있는 j의 값을 더한 값과, 현재의 값을 비교
    # print(count)
print(max(count))