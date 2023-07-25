
T = int(input())
num = 0
def check(NTP):
    while len(NTP)>0:
        it = NTP[0]
        try:
            while True:
                x = NTP.index(it)
                NTP.remove(it)
                if x != 0:
                    return 0
        except ValueError:
            continue
    return 1

for i in range(T):
    M = list(input())
    num += check(M)
    
print(num)