# 역케이스 ' ' 공백 하나인 경우 틀림
Sen = input()
count = 1
for i in Sen[1:-1]:
    if i == ' ':
        count += 1
        
print(count)