N = int(input())
switchList = list(map(int,input().split()))

personN = int(input())
for _ in range(personN):
    gen, num = map(int, input().split())

    if gen == 1:
        for i in range(num-1, N, num):
            switchList[i] = (switchList[i] + 1) % 2
    elif gen == 2:
        location = 0
        while 0<=num-1-location and num-1+location<N and switchList[num-1-location] == switchList[num-1+location]:
            switchList[num-1-location] = (switchList[num-1-location] + 1) % 2
            switchList[num-1+location] = switchList[num-1-location]
            location += 1

for number in range(1, N+1):
    print(switchList[number-1], end=' ')
    if number % 20 == 0:
        print()
