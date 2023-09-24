
def generate(result, n):
    if n == r:
        results.append(result[:])
        return
    for i in range(len(arr)):
        if not used[i]:
            used[i] = True
            result.append(arr[i])
            generate(result, n + 1)
            result.pop()
            used[i] = False


# 예제
arr = [1, 2, 3]
r = 2
results = []
used = [False] * len(arr)
generate([], 0)
permutation_list = results
print(permutation_list)