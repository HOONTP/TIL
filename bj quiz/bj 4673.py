def DRK(num):
    
    SUM = sum(int(i) for i in str(num))
    nums = num + SUM
    keys.append(num)
    values.append(nums)
    Total_case[num] = nums
    
    return

Total_case = {}
keys = []
values = []
for i in range(1, 10000):
    (DRK(i))

for it in range(1,10001):
    if it not in values:
        print(it)