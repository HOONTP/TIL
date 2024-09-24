numbers = str(input())

numList = list(0 for _ in range(9))

for i in range(len(numbers)):
    if numbers[i] == '9':
        numList[6] += 1
    else:
        numList[int(numbers[i])] += 1
A = (numList[6]+1) // 2
numList[6] = A
print(max(numList))