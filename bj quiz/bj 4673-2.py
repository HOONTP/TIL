def DRK(num):
    
    SUM = sum(int(i) for i in str(num))
    nums = num + SUM
    values.append(nums)
    return

values = []

for i in range(1, 10001):
    (DRK(i))

for it in range(1,10001):
    if it not in values:
        print(it)