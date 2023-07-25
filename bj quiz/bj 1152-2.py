Sen = input().strip()
count = 0

if Sen:  # 입력이 공백 문자열이 아닌 경우에만 실행
    count = 1  # 첫 번째 단어를 세기 위해 초기값을 1로 설정

    for i in Sen:
        if i == ' ':
            count += 1

print(count)