import sys
# sys.stdin = open('input.in')
input = sys.stdin.readline

N = int(input())

num = int(N**0.5)
print(num)

#약수의 각 (지수+1)을 곱한 것이 문이 열리고 닫히는 횟수이다.
#즉, 제곱수만 2+1회로 열 닫 열 => 열려 있고 나머지는 닫혀있다.
#N을 루트 씌운 값이 그 아래의 제곱수의 갯수와 같다.