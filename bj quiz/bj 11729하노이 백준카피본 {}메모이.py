memo = {}


def hanoi(value, start, finish, support):
    key = (value, start, finish, support)
    if key in memo:
        return memo[key]
    if value == 1:
        return f"{start} {finish}"
    if value >= 2:
        output = "\n".join(
            [hanoi(value - 1, start, support, finish), f"{start} {finish}", hanoi(value - 1, support, finish, start)])
        memo[key] = output
        return output


num = int(input())
print(f"{2 ** num - 1}")
print(hanoi(num, "1", "3", "2"))