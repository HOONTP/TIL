def make_num(num):
    nums = sum(int(i) for i in str(num))
    return nums + num
    pass


N = int(input())
val = 0
for i in range(1, N+1):
    val = (make_num(i))
    if val == N:
        print(i)
        quit()

print(0)

# ## 중요 아래 9*k를 하는 이유 최대한 멀리 가봐야 9*k만큼이다 <- 한자리당9씩 멀어짐
# if N>=9*k:
#     for i in range(N -9*k,N+1):
#         n = i
#         p = str(i)
#         for j in range(0, len(p)):
#             n += int(p[j])
#         if n==N:
#             print(i)
#             quit()


### 1번 제출
def make_num(num):
    nums = sum(int(i) for i in str(num))
    return num, nums + num
    pass


N = int(input())
lst = []
for i in range(1,N+1):
    lst.append(make_num(i))

cnt = 0

for it in lst:
    if it[1] == N:
        print(it[0])
        cnt += 1
        break

if cnt == 0:
    print('0')