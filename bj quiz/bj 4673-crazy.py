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
for i in range(1, 1000):
    (DRK(i))

for it in values:
    if values.count(it) == 1:
        for ic in keys:
            if ic < 100 and Total_case[ic] == it:
                print(ic, it)

# for nm in del_case:
#     if nm > 10000:
#         break
#     print(nm)