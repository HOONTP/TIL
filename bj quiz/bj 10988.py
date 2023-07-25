voca = input()
def check(word):
    leng = len(word) // 2
    if len(word) % 2 == 1:
        if word[:leng] == word[:leng:-1]:
            return 1
        
    elif len(word) % 2 == 0:
        if word[:leng] == word[:leng-1:-1]:
            return 1
    return 0

print(check(voca.strip()))