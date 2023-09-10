import sys
input = sys.stdin.readline

def binary_search():
    start = 1
    end = lst[-1] - lst[0]

    while start <= end:

        mid = (left + right) // 2  # 중간 인덱스 계산

        if arr[mid] == target:
            return mid  # 원하는 값이 발견됨
        elif arr[mid] < target:
            left = mid + 1  # 중간 값보다 오른쪽에 위치
        else:
            right = mid - 1  # 중간 값보다 왼쪽에 위치

    return -1  # 원하는 값이 리스트에 없음

N, C = map(int, input().split())

lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort()

result = binary_search()

if result != -1:
    print(f"7은 인덱스 {result}에서 찾았습니다.")
else:
    print("7을 찾을 수 없습니다.")

